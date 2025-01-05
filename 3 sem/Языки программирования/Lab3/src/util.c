#include <inttypes.h>
#include <stdint.h>
#include <string.h>

#include "../include/util.h"


enum check_transformation_status check_transformation(char* message) {
    const char* transformation_list[] = {"none", "cw90", "ccw90", "fliph", "flipv"};
    int list_size = sizeof(transformation_list) / sizeof(transformation_list[0]);
    for (int i = 0; i < list_size; i++) {
        if (strcmp(message, transformation_list[i]) == 0) {
            return CHECK_TRANSFORMATION_OK;
        }
    }
    return CHECK_TRANSFORMATION_ERROR;
}


uint32_t padding(uint32_t width) {
    while (width % 4 != 0){
        width += 1;
    }
    return width;
}


enum transformation_type get_transformation_type(char* message) {
    if (strcmp(message, "none") == 0) return TRANSFORMATION_TYPE_NONE;
    if (strcmp(message, "cw90") == 0) return TRANSFORMATION_TYPE_CW90;
    if (strcmp(message, "ccw90") == 0) return TRANSFORMATION_TYPE_CCW90;
    if (strcmp(message, "fliph") == 0) return TRANSFORMATION_TYPE_FLIPH;
    if (strcmp(message, "flipv") == 0) return TRANSFORMATION_TYPE_FLIPV;
    return TRANSFORMATION_TYPE_ERROR;
}
