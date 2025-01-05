#ifndef OPEN_CLOSE_H
    #define OPEN_CLOSE_H
    #include <stdio.h>

    enum open_status {
        OPEN_OK = 0,
        OPEN_ERROR
    };

    struct maybe_open_file {
        enum open_status status;
        FILE* file;
    };

    struct maybe_open_file open_source_file(const char* filename);
    struct maybe_open_file open_transformed_file(const char* filename);

    enum close_status {
        CLOSE_OK = 0,
        CLOSE_ERROR
    };
    
    enum close_status close_file(FILE* file);
#endif
