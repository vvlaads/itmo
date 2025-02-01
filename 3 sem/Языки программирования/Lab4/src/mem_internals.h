#ifndef _MEM_INTERNALS_
#define _MEM_INTERNALS_

#include <inttypes.h>
#include <stdbool.h>
#include <stddef.h>

#define REGION_MIN_SIZE (2 * 4096) //минимальный размер региона
#define BLOCK_ALIGN 16 //выравнивание содержания блока

//структура региона
struct region {
  void* addr; //адрес начала региона
  size_t size; //размер региона в байтах
  bool extends; //регион является продолжением
};

static const struct region REGION_INVALID = {0}; //пустой регион


/*проверяет валидность региона
получает указатель на регион
возвращает true, если регион некорректен*/
inline bool region_is_invalid( const struct region* r ) { return r->addr == NULL; }


typedef struct { size_t bytes; } block_capacity; //вместимость блока в байтах

typedef struct { size_t bytes; } block_size; //размер блока в байтах (вместимость + размер заголовка)


//структура для работы с блоками данных
struct __attribute__((packed)) block_header {
  struct block_header*    next; //указатель на следующий блок
  block_capacity capacity; //вместимость блока
  bool           is_free; //состояние блока (свободен/занят)
  uint8_t contents[]; //массив с данными
};


/*определяет размер блока по его вместимости
получает вместимость блока
возвращает размер блока (вместимость + размер заголовка)*/
inline block_size size_from_capacity( block_capacity cap ) { return (block_size) {cap.bytes + offsetof( struct block_header, contents ) }; }


/*определяет вместимость блока по его размеру
получает размер блока (вместимость + размер заголовка)
возвращает вместимость блока*/
inline block_capacity capacity_from_size( block_size sz ) { return (block_capacity) {sz.bytes - offsetof( struct block_header, contents ) }; }
#endif
