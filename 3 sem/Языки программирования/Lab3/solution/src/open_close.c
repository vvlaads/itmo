#include <stdio.h>

#include "../include/open_close.h"

//открываем файл на чтение
struct maybe_open_file open_source_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        return (struct maybe_open_file) {.status = OPEN_ERROR};
    }
    return (struct maybe_open_file) {.status = OPEN_OK, .file = file};
}

//открываем файл на запись
struct maybe_open_file open_transformed_file(const char* filename) {
    FILE* file = fopen(filename, "w+");
    if (file == NULL) {
        return (struct maybe_open_file) {.status = OPEN_ERROR};
    }
    return (struct maybe_open_file) {.status = OPEN_OK, .file = file};
}

//закрываем файл
enum close_status close_file(FILE* file) {
    int result = fclose(file);
    if (result == 0) {
        return CLOSE_OK;
    }
    return CLOSE_ERROR;
}
