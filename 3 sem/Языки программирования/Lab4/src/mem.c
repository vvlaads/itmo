#define _DEFAULT_SOURCE

#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

#include "mem.h"
#include "mem_internals.h"
#include "util.h"


void debug_block(struct block_header* b, const char* fmt, ... );


void debug(const char* fmt, ... );


extern inline block_size size_from_capacity(block_capacity cap);


extern inline block_capacity capacity_from_size(block_size sz);


/*проверяет, может ли блок вместить указанное количество байт
получает размер для проверки, указатель на блок
возвращает true, если блок может вместить указанное количество байт*/
static bool block_is_big_enough(size_t query, struct block_header* block) {
  return block->capacity.bytes >= query;
}


/*определяет количество страниц памяти для хранения указанного количества байт
получает количество байт
возвращает количество страниц памяти*/
static size_t pages_count(size_t mem) {
  if (mem == 0) {
    return 0;
  }
  return mem / getpagesize() + ((mem % getpagesize()) > 0);
}


/*определяет сколько суммарно байт занимают страницы, вмещающие указанное количество байт
получает количество байт
возвращает суммарное количество байт выделенных страниц*/
static size_t round_pages(size_t mem) {
  return getpagesize() * pages_count( mem );
}


/*инициализирует свободный блок по указанному адресу
получает адрес для размещения блока, размер блока, указатель на следующий блок*/
static void block_init(void* restrict addr, block_size block_sz, void* restrict next) {
  *((struct block_header*)addr) = (struct block_header) {
    .next = next,
    .capacity = capacity_from_size(block_sz),
    .is_free = true
  };
}


/*определяет размер региона для хранения указанного количества байтов
получает количество байт, для которых нужно выделить память
возвращает размер региона в байтах*/
static size_t region_actual_size(size_t query) {
  return size_max(round_pages(query), REGION_MIN_SIZE);
}


extern inline bool region_is_invalid(const struct region* r);


/*выделяет блок памяти
получает адрес размещения в памяти, количество байт для выделения, флаги поведения отображения
возвращает указатель на начало выделенной памяти*/
static void* map_pages(void const* addr, size_t length, int additional_flags) {
  return mmap( (void*) addr, length, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | additional_flags , -1, 0 );
}


/*  аллоцировать регион памяти и инициализировать его блоком */
static struct region alloc_region(void const * addr, size_t query) {
  bool extends = true;
  block_capacity capacity = {.bytes = query};
  size_t size_for_region = region_actual_size(size_from_capacity(capacity).bytes);
  void* addr_for_region = map_pages(addr, size_for_region, MAP_FIXED_NOREPLACE);

  if (addr_for_region == MAP_FAILED) {
    addr_for_region = map_pages(addr, size_for_region, 0);
    extends = false;
  }

  if (addr_for_region == MAP_FAILED) {
    return REGION_INVALID;
  }

  struct region region = {.addr = addr_for_region, .size = size_for_region, .extends = extends};
  block_size block_size = {.bytes = size_for_region};
  block_init(addr_for_region, block_size, NULL);
  return region;
}


/*связывает текущий блок и следующий
получает указатель на текущий блок
возвращает указатель на следующий блок*/
static void* block_after(struct block_header const* block);


/*определяет, является ли второй блок следующим после первого
получает указатель на первый блок, указатель на второй блок
возвращает true, если второй блок идёт сразу за первым*/
static bool blocks_continuous (struct block_header const* fst, struct block_header const* snd);


/*инициализирует кучу
получает размер кучи в байтах
возвращает указатель на начало кучи*/
void* heap_init(size_t initial) {
  const struct region region = alloc_region( HEAP_START, initial );
  if ( region_is_invalid(&region) ) return NULL;

  return region.addr;
}



#define EXIT_ERROR 1 //код ошибки


/*  освободить всю память, выделенную под кучу */
void heap_term() {
  size_t region_size = 0;
  struct block_header* block = (struct block_header*)HEAP_START;
  struct block_header* region = (struct block_header*)HEAP_START;

  while(block) {
    region_size += size_from_capacity(block->capacity).bytes;

    if (blocks_continuous(block, block->next)) {
      block = block->next;
    }

    else {
      struct block_header* next_block = block->next;
      if (munmap(region, region_size) != 0) {
        exit(EXIT_ERROR);
      }
      block = next_block;
      region = next_block;
      region_size = 0;
    }
  }
}


#define BLOCK_MIN_CAPACITY 24 //минимальная вместимость блока



/*  --- Разделение блоков (если найденный свободный блок слишком большой )--- */


/*определяет можно ли разделить блок на более мелкие
получает указатель на блок, количество байт, которые хотим записать
возвращает true, если блок можно разбить на части*/
static bool block_splittable( struct block_header* restrict block, size_t query) {
  return block-> is_free && query + offsetof( struct block_header, contents ) + BLOCK_MIN_CAPACITY <= block->capacity.bytes;
}


/*разделяет блоки, если его размер слишком большой
получает указатель на блок, количество байт для проверки
возвращает true, если блок был разделен*/
static bool split_if_too_big( struct block_header* block, size_t query ) {
  if (block_splittable(block, query)) {
    size_t old_block_capacity_bytes = size_max(query, BLOCK_MIN_CAPACITY);
    block_capacity old_block_capacity = {.bytes = old_block_capacity_bytes};
    struct block_header* next_block = block->next;

    size_t new_block_size_bytes = block->capacity.bytes - old_block_capacity_bytes;
    block_size new_block_size = {.bytes = new_block_size_bytes};
    if (new_block_size.bytes < offsetof(struct block_header, contents) + BLOCK_MIN_CAPACITY) {
      return false;
    }
    block->capacity = old_block_capacity;
    block->next = block_after(block);
    block_init(block->next, new_block_size, next_block);
    return true;
  }
  return false;
}



/*  --- Слияние соседних свободных блоков --- */


static void* block_after(struct block_header const* block) {
  return  (void*) (block->contents + block->capacity.bytes);
}


static bool blocks_continuous (struct block_header const* fst, struct block_header const* snd) {
  return (void*)snd == block_after(fst);
}


/*определяет, можно ли объеденить блоки в один
получает указатель на первый блок, указатель на второй блок
возвращает true, если блоки можно объеденить*/
static bool mergeable(struct block_header const* restrict fst, struct block_header const* restrict snd) {
  return fst->is_free && snd->is_free && blocks_continuous( fst, snd ) ;
}


/*пытается объеденить текущий блок со следующим
получает указатель на текущий блок
возвращает true, если удалось объеденить блоки*/
static bool try_merge_with_next( struct block_header* block ) {
  if (block == NULL || block->next == NULL) {
    return false;
  }

  struct block_header* next_block = block->next;
  if (mergeable(block, next_block)) {
    block_capacity merged_block_capacity = {.bytes = (block->capacity.bytes + size_from_capacity(next_block->capacity).bytes)};
    block->capacity = merged_block_capacity;
    block->next = next_block->next;
    return true;
  }

  return false;
}



/*  --- ... ecли размера кучи хватает --- */


//структура для поиска блоков
struct block_search_result {
  enum {
    //найден хороший блок
    BSR_FOUND_GOOD_BLOCK,
    //подходящий блок не найден
    BSR_REACHED_END_NOT_FOUND, 
    //ошибка поиска
    BSR_CORRUPTED
  } type; //статус поиска

  struct block_header* block; //указатель на блок
};


/*ищет блок, вмещающий указанное количество байт
получает указатель на первый блок, количество байт
возвращает результат поиска блока*/
static struct block_search_result find_good_or_last(struct block_header* restrict block, size_t sz) {
  struct block_search_result result;

  //проверка, что передан корректный указатель
  if (block == NULL) {
    result = (struct block_search_result){.type = BSR_CORRUPTED, .block = block};
    return result;
  }

  while (block) {
    if (block->is_free) {
      while (try_merge_with_next(block)); //объединяем пустые блоки

      //если блок вмещает необходимое число байт
      if (block_is_big_enough(sz, block)) {
        result = (struct block_search_result){.type = BSR_FOUND_GOOD_BLOCK, .block = block};
        return result;
      }
    }

    //выходим на последнем существующем блоке
    if (block->next == NULL) {
      break;
    }

    block = block->next;
  }

  result = (struct block_search_result){.type = BSR_REACHED_END_NOT_FOUND, .block = block};
  return result;
}


/*  Попробовать выделить память в куче начиная с блока `block` не пытаясь расширить кучу
 Можно переиспользовать как только кучу расширили. */
static struct block_search_result try_memalloc_existing ( size_t query, struct block_header* block ) {
  struct block_search_result find_good_block = find_good_or_last(block, query); //пытаемся найти хороший блок

  //если нашли, то помечаем его, как занятый
  if (find_good_block.type == BSR_FOUND_GOOD_BLOCK) {
    struct block_header* good_block = find_good_block.block;
    split_if_too_big(good_block, query);
    good_block->is_free = false;
  }

  return find_good_block;
}


/*увеличивает размер кучи
получает указатель на последний блок в куче, количестов байт
возвращает первый блок, дополняющий кучу*/
static struct block_header* grow_heap( struct block_header* restrict last, size_t query ) {
  //проверка, что передан правильный последний блок
  if (last == NULL) {
    return NULL;
  }

  struct region new_region = alloc_region(block_after(last), query);

  //проверка, что регион был выделен
  if (region_is_invalid(&new_region)) {
    return NULL;
  }
  struct block_header* new_block = new_region.addr;
  last->next = new_block;

  if(new_region.extends && try_merge_with_next(last)) {
    return last;
  }
  
  return new_region.addr;
}


/*  Реализует основную логику malloc и возвращает заголовок выделенного блока */
static struct block_header* memalloc( size_t query, struct block_header* heap_start) {
  query = size_max(query, BLOCK_MIN_CAPACITY);
  struct block_search_result find_good_block = try_memalloc_existing(query, heap_start); //пытаемся найти хороший блок

  if (find_good_block.type == BSR_CORRUPTED) {
    return NULL;
  }

  else if (find_good_block.type == BSR_REACHED_END_NOT_FOUND) {
    struct block_header* block_in_heap_continue = grow_heap(find_good_block.block, query);

    if (block_in_heap_continue == NULL) {
      return NULL;
    }

    find_good_block = try_memalloc_existing(query, block_in_heap_continue);

    if (find_good_block.type != BSR_FOUND_GOOD_BLOCK) {
      return NULL;
    }

    return find_good_block.block;
  }

  return find_good_block.block;
}


/*динамически выделяет память
получает количество байт
возвращает указатель на массив, если удалось выделить память*/
void* _malloc( size_t query ) {
  struct block_header* const addr = memalloc( query, (struct block_header*) HEAP_START );
  if (addr) return addr->contents;
  else return NULL;
}


/*получает начало блока по указателю на его массив с данными
получает указатель на массив данных
возвращает указатель на начало блока*/
static struct block_header* block_get_header(void* contents) {
  return (struct block_header*) (((uint8_t*)contents)-offsetof(struct block_header, contents));
}


/*освобождает динамическую память
получает указатель на массив с данными*/
void _free( void* mem ) {
  if (!mem) return ;
  struct block_header* header = block_get_header( mem );
  header->is_free = true;
  while (try_merge_with_next(header));
}
