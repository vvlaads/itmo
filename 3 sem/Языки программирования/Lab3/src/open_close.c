#include <stdio.h>

#include "../include/open_close.h"

struct maybe_open_file open_source_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        return (struct maybe_open_file) {.status = OPEN_ERROR};
    }
    return (struct maybe_open_file) {.status = OPEN_OK, .file = file};
}


struct maybe_open_file open_transformed_file(const char* filename) {
    FILE* file = fopen(filename, "w+");
    if (file == NULL) {
        return (struct maybe_open_file) {.status = OPEN_ERROR};
    }
    return (struct maybe_open_file) {.status = OPEN_OK, .file = file};
}


enum close_status close_file(FILE* file) {
    int result = fclose(file);
    if (result == 0) {
        return CLOSE_OK;
    }
    return CLOSE_ERROR;
}
