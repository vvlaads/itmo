#ifndef UTIL_H
    #define UTIL_H
    #include <string.h>
    #include <inttypes.h>

    enum check_transformation_status {
        CHECK_TRANSFORMATION_OK = 0,
        CHECK_TRANSFORMATION_ERROR
    };
    
    enum check_transformation_status check_transformation(char* message);

    uint32_t padding(uint32_t width);


    enum transformation_type {
        TRANSFORMATION_TYPE_NONE = 0,
        TRANSFORMATION_TYPE_CW90,
        TRANSFORMATION_TYPE_CCW90,
        TRANSFORMATION_TYPE_FLIPH,
        TRANSFORMATION_TYPE_FLIPV,
        TRANSFORMATION_TYPE_ERROR
    };

    enum transformation_type get_transformation_type(char* message);
#endif
