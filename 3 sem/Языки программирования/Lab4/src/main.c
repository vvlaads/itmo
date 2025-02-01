#include <stdio.h>

#include "my_tests.h"


static inline void print_my_separator() {
	printf("---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n");
}

int main() {
	printf("Запуск тестов\n");

	print_my_separator();
	check_test_success_mem_alloc();

	print_my_separator();
	check_test_free_one_block();

	print_my_separator();
	check_test_free_two_blocks();

	print_my_separator();
	check_test_create_new_region();

	print_my_separator();
	check_test_create_new_region_in_different_place();

	print_my_separator();
	return 0;
}
