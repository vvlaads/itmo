#ifndef BMP_CONVERTER_H
    #define BMP_CONVERTER_H
    #include <stdio.h>
    #include <stdlib.h>
    #include <stdint.h>
    #include <inttypes.h>
    
    #include "../include/image.h"

    enum read_status  {
        READ_OK = 0,
        READ_INVALID_SIGNATURE,
        READ_INVALID_BITS,
        READ_INVALID_HEADER,
        READ_OUT_OF_MEMORY,
        READ_INITIALIZATION
    };

    enum read_status from_bmp( FILE* in, struct image* img );

    enum  write_status  {
        WRITE_OK = 0,
        WRITE_ERROR,
        WRITE_OUT_OF_MEMORY
    };
    
    enum write_status to_bmp( FILE* out, struct image const* img ); 
#endif
