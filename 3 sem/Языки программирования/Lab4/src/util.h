#ifndef _UTIL_H_
#define _UTIL_H_

#include <stddef.h>

/*определяет наибольший размер
получает два размера для сравнения
возвращает наибольший размер*/
inline size_t size_max( size_t x, size_t y ) { return (x >= y)? x : y ; }


/*вывод ошибки и завершение программы
получает аргументы для вывода информации об ошибке*/
_Noreturn void err( const char* msg, ... );
#endif
