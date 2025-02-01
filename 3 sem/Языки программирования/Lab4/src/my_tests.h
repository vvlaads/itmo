#ifndef MY_TESTS_H
	#define MY_TESTS_H

	#include <stdio.h>

	#define TEST_HEAP_SIZE 3000 //Тестовая вместимость кучи
	#define TEST_BLOCK_SIZE 16 //Размер блока для тестирования
	#define TEST_BIG_BLOCK_SIZE 16000 //Размер блока, превышающий размер кучи
	#define TEST_BYTE 42 //Байт для проверки значений
	#define TEST_REGION_SIZE 4; //Размер региона для тестирования
	#define TEST_ZERO 0 //Ноль для проверки значений
	#define REGION_MIN_SIZE (2 * 4096) //минимальный размер региона
	#define MAP_ANONYMOUS 0x20 //Флаг для mmap
	


	/*запускает тест по проверке выделения памяти*/
	void check_test_success_mem_alloc();


	/*запускает тест по проверке освобождения одного блока из нескольких выделенных*/
	void check_test_free_one_block();


	/*запускает тест по проверке освобождения двух блоков из нескольких выделенных*/
	void check_test_free_two_blocks();


	/*запускает тест по проверке выделения региона, когда закончилась память*/
	void check_test_create_new_region();

	/*запускает тест по проверке выделения региона, когда закончилась память и нельзя расширить предыдущий*/
	void check_test_create_new_region_in_different_place();
#endif
