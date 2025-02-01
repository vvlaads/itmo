#include <inttypes.h>
#include <stdint.h>

#include "my_tests.h"
#include "mem.h"



//статус проверки успешного выделения памяти
enum result_success_mem_alloc {
	//память выделена успешно
	SUCCESS_MEM_ALLOC_OK = 0,
	//указатель на начало кучи равен NULL
	SUCCESS_MEM_ALLOC_NULL_HEAP,
	//указатель на область равен NULL
	SUCCESS_MEM_ALLOC_NULL_PTR,
	//ошибка выделения памяти
	SUCCESS_MEM_ALLOC_ERROR
};


/*проверяет выделение памяти
возвращает статус проверки*/
static enum result_success_mem_alloc test_success_mem_alloc() {
	size_t heap_size = TEST_HEAP_SIZE;
	uint8_t* heap = heap_init(heap_size);
	printf("Адрес начала кучи: %p\n", heap);

	if (heap == NULL) {
		return SUCCESS_MEM_ALLOC_NULL_HEAP;
	}

	size_t test_size = TEST_BLOCK_SIZE;
	uint8_t* ptr = _malloc(test_size);
	printf("Адрес начала блока: %p\n", ptr);

	if (ptr == NULL) {
		heap_term();
		return SUCCESS_MEM_ALLOC_NULL_PTR;
	}

	heap_term();
	return SUCCESS_MEM_ALLOC_OK;
}


void check_test_success_mem_alloc() {
	printf("Запуск теста 1\n");
	enum result_success_mem_alloc result = test_success_mem_alloc();
	switch(result) {
		case SUCCESS_MEM_ALLOC_OK: {
			printf("Тест пройден\n");
			break;
		}
		case SUCCESS_MEM_ALLOC_NULL_PTR: {
			printf("Указатель при выделении памяти равен NULL\n");
			break;
		}
		case SUCCESS_MEM_ALLOC_NULL_HEAP: {
			printf("Указатель на начало кучи при выделении памяти равен NULL\n");
			break;
		}
		case SUCCESS_MEM_ALLOC_ERROR: {
			printf("Ошибка выделения памяти\n");
			break;
		}
	}
}


//статус проверки освобождения одного блока из нескольких выделенных
enum result_free_one_block {
	//Блок успешно освобожден
	FREE_ONE_BLOCK_OK = 0,
	//Ошибка выделения памяти под кучу
	FREE_ONE_BLOCK_NULL_HEAP,
	//Ошибка выделения памяти под один из блоков
	FREE_ONE_BLOCK_NULL_BLOCK,
	//Ошибка освобождения блока
	FREE_ONE_BLOCK_ERROR
};


/*проверяет освобождение одного блока из нескольких выделенных
возвращает статус проверки*/
static enum result_free_one_block test_free_one_block() {
	size_t heap_size = TEST_HEAP_SIZE;
	uint8_t* heap = heap_init(heap_size);
	printf("Адрес начала кучи: %p\n", heap);

	if (heap == NULL) {
		return FREE_ONE_BLOCK_NULL_HEAP;
	}

	size_t test_size = TEST_BLOCK_SIZE;
	uint8_t* block1 = _malloc(test_size);
	uint8_t* block2 = _malloc(test_size);
	uint8_t* block3 = _malloc(test_size);
	printf("Адрес начала первого блока: %p\n", block1);
	printf("Адрес начала второго блока: %p\n", block2);
	printf("Адрес начала третьего блока: %p\n", block3);

	if (block1 == NULL || block2 == NULL || block3 == NULL) {
		heap_term();
		return FREE_ONE_BLOCK_NULL_BLOCK;
	}

	_free(block2);
	printf("Освобождение блока с адресом: %p\n", block2);

	uint8_t* test_block = _malloc(test_size);
	printf("Адрес блока для проверки: %p\n", test_block);

	if (block2 == test_block) {
		heap_term();
		return FREE_ONE_BLOCK_OK;
	}

	heap_term();
	return FREE_ONE_BLOCK_ERROR;
}


void check_test_free_one_block() {
	printf("Запуск теста 2\n");
	enum result_free_one_block result = test_free_one_block();
	switch(result) {
		case FREE_ONE_BLOCK_OK: {
			printf("Тест пройден\n");
			break;
		}
		case FREE_ONE_BLOCK_NULL_HEAP: {
			printf("Ошибка выделения памяти под кучу\n");
			break;
		}
		case FREE_ONE_BLOCK_NULL_BLOCK: {
			printf("Ошибка выделения памяти одного из блоков\n");
			break;
		}
		case FREE_ONE_BLOCK_ERROR: {
			printf("Ошибка освобождения блока\n");
			break;
		}
	}
}


//статус проверки освобождения двух блоков из нескольких выделенных
enum result_free_two_blocks {
	//Два блока успешно освобождены
	FREE_TWO_BLOCKS_OK = 0,
	//Ошибка выделения памяти под кучу
	FREE_TWO_BLOCKS_NULL_HEAP,
	//Ошибка выделения памяти под один из блоков
	FREE_TWO_BLOCKS_NULL_BLOCK,
	//Ошибка освобождения двух блоков
	FREE_TWO_BLOCKS_ERROR
};


/*проверяет освобождение двух блоков из нескольких выделенных
возвращает статус проверки*/
static enum result_free_two_blocks test_free_two_blocks() {
	size_t heap_size = TEST_HEAP_SIZE;
	uint8_t* heap = heap_init(heap_size);
	printf("Адрес начала кучи: %p\n", heap);

	if (heap == NULL) {
		return FREE_TWO_BLOCKS_NULL_HEAP;
	}

	size_t test_size = TEST_BLOCK_SIZE;
	uint8_t* block1 = _malloc(test_size);
	uint8_t* block2 = _malloc(test_size);
	uint8_t* block3 = _malloc(test_size);
	printf("Адрес начала первого блока: %p\n", block1);
	printf("Адрес начала второго блока: %p\n", block2);
	printf("Адрес начала третьего блока: %p\n", block3);
	

	if (block1 == NULL || block2 == NULL || block3 == NULL) {
		heap_term();
		return FREE_TWO_BLOCKS_NULL_BLOCK;
	}

	_free(block2);
	printf("Освобождение блока с адресом: %p\n", block2);

	_free(block3);
	printf("Освобождение блока с адресом: %p\n", block3);

	uint8_t* test_block2 = _malloc(test_size);
	printf("Адрес первого блока для проверки: %p\n", test_block2);
	uint8_t* test_block3 = _malloc(test_size);
	printf("Адрес второго блока для проверки: %p\n", test_block3);

	if (test_block2 == block2 && test_block3 == block3) {
		heap_term();
		return FREE_TWO_BLOCKS_OK;
	}

	heap_term();
	return FREE_TWO_BLOCKS_ERROR;
}


void check_test_free_two_blocks() {
	printf("Запуск теста 3\n");
	enum result_free_two_blocks result = test_free_two_blocks();
	switch(result) {
		case FREE_TWO_BLOCKS_OK: {
			printf("Тест пройден\n");
			break;
		}
		case FREE_TWO_BLOCKS_NULL_HEAP: {
			printf("Ошибка выделения памяти для кучи\n");
			break;
		}
		case FREE_TWO_BLOCKS_NULL_BLOCK: {
			printf("Ошибка выделения памяти для одного из блоков\n");
			break;
		}
		case FREE_TWO_BLOCKS_ERROR: {
			printf("Ошибка освобождения двух блоков\n");
			break;
		}
	}
}


//статус проверки выделения региона, когда закончилась память
enum result_create_new_region {
	//Регион выделен верно
	CREATE_NEW_REGION_OK = 0,
	//Ошибка выделения памяти для кучи
	CREATE_NEW_REGION_NULL_HEAP,
	//Ошибка выделения памяти для блока
	CREATE_NEW_REGION_NULL_BLOCK,
	//Ошибка выделения региона
	CREATE_NEW_REGION_ERROR
};


/*проверяет выделение региона, когда закончилась память
возвращает статус проверки*/
static enum result_create_new_region test_create_new_region() {
	size_t heap_size = TEST_HEAP_SIZE;
	uint8_t* heap = heap_init(heap_size);
	printf("Адрес начала кучи: %p\n", heap);

	if (heap == NULL) {
		return CREATE_NEW_REGION_NULL_HEAP;
	}

	size_t big_block_size = TEST_BIG_BLOCK_SIZE;
	uint8_t* big_block = _malloc(big_block_size);
	printf("Адрес начала большого блока: %p\n", big_block);

	if (big_block == NULL) {
		heap_term();
		return CREATE_NEW_REGION_NULL_BLOCK;
	}

	for (size_t i = 0; i < big_block_size; i++) {
		big_block[i] = TEST_BYTE;
	}

	uint8_t* after_heap = HEAP_START + heap_size + 1;
	printf("Адрес следующего региона: %p\n", after_heap);

	if (*after_heap == (uint8_t)TEST_BYTE) {
		heap_term();
		return CREATE_NEW_REGION_OK;
	}

	printf("Ожидаемое число: %" PRIu8 "\n", (uint8_t)TEST_BYTE);
	printf("Реальное число: %" PRIu8 "\n", *after_heap);

	heap_term();
	return CREATE_NEW_REGION_ERROR;
}


void check_test_create_new_region() {
	printf("Запуск теста 4\n");
	enum result_create_new_region result = test_create_new_region();
	switch(result) {
		case CREATE_NEW_REGION_OK: {
			printf("Тест пройден\n");
			break;
		}
		case CREATE_NEW_REGION_NULL_HEAP: {
			printf("Ошибка выделения памяти для кучи\n");
			break;
		}
		case CREATE_NEW_REGION_NULL_BLOCK: {
			printf("Ошибка выделения памяти для блока\n");
			break;
		}
		case CREATE_NEW_REGION_ERROR: {
			printf("Ошибка выделения региона памяти\n");
			break;
		}
	}
}


//статус проверки выделения региона, когда закончилась память и нельзя расширить предыдущий
enum result_create_new_region_in_different_place {
	//Регион выделен верно
	CREATE_NEW_REGION_IN_DIFFERENT_PLACE_OK = 0,
	//Ошибка выделения памяти для кучи
	CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_HEAP,
	//Ошибка выделения региона памяти после кучи
	CREATE_NEW_REGION_IN_DIFFERENT_PLACE_TEST_BLOCK,
	//Ошибка выделения памяти для блока
	CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_BLOCK,
	//Ошибка выделения региона
	CREATE_NEW_REGION_IN_DIFFERENT_PLACE_ERROR
};


/*проверяет выделение региона, когда закончилась память и нельзя расширить предыдущий
возвращает статус проверки*/
static enum result_create_new_region_in_different_place test_create_new_region_in_different_place() {
	size_t heap_size = TEST_HEAP_SIZE;
	uint8_t* heap = heap_init(heap_size);
	printf("Адрес начала кучи: %p\n", heap);

	if (heap == NULL) {
		return CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_HEAP;
	}

	uint8_t* after_heap = HEAP_START + REGION_MIN_SIZE;
	size_t test_region_size = TEST_REGION_SIZE;
	after_heap = mmap((void*) after_heap, test_region_size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED, -1, 0);
	printf("Адрес начала занятого региона памяти после кучи: %p\n", after_heap);

	if (after_heap == MAP_FAILED) {
		heap_term();
		return CREATE_NEW_REGION_IN_DIFFERENT_PLACE_TEST_BLOCK;
	}

	size_t big_block_size = TEST_BIG_BLOCK_SIZE;
	uint8_t* big_block = _malloc(big_block_size);
	printf("Адрес начала большого блока: %p\n", big_block);

	if (big_block == NULL) {
		munmap(after_heap, test_region_size);
		heap_term();
		return CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_BLOCK;
	}

	for (size_t i = 0; i < big_block_size; i++) {
		big_block[i] = (uint8_t)TEST_BYTE;
	}

	for (size_t i = 0; i < heap_size; i++) {
		after_heap[i] = (uint8_t)TEST_ZERO;
	}

	if (big_block[heap_size + 1] == (uint8_t)TEST_BYTE) {
		munmap(after_heap, test_region_size);
		heap_term();
		return CREATE_NEW_REGION_IN_DIFFERENT_PLACE_OK;
	}

	printf("Ожидаемое число: %" PRIu8 "\n", (uint8_t)TEST_BYTE);
	printf("Реальное число: %" PRIu8 "\n", big_block[heap_size + 1]);

	munmap(after_heap, test_region_size);
	heap_term();
	return CREATE_NEW_REGION_IN_DIFFERENT_PLACE_ERROR;
}


void check_test_create_new_region_in_different_place() {
	printf("Запуск теста 5\n");
	enum result_create_new_region_in_different_place result = test_create_new_region_in_different_place();
	switch(result) {
		case CREATE_NEW_REGION_IN_DIFFERENT_PLACE_OK: {
			printf("Тест пройден\n");
			break;
		}
		case CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_HEAP: {
			printf("Ошибка выделения памяти для кучи\n");
			break;
		}
		case CREATE_NEW_REGION_IN_DIFFERENT_PLACE_TEST_BLOCK: {
			printf("Ошибка выделения памяти после кучи\n");
			break;
		}
	case CREATE_NEW_REGION_IN_DIFFERENT_PLACE_NULL_BLOCK: {
			printf("Ошибка выделения памяти для блока\n");
			break;
		}
		case CREATE_NEW_REGION_IN_DIFFERENT_PLACE_ERROR: {
			printf("Ошибка выделения региона памяти\n");
			break;
		}
	}
}
