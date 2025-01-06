#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "../include/image.h"
#include "../include/transformation_none.h"


struct maybe_transformation_image transformation_none(const struct image* source) {
    struct image* new_image = create_image();

    //проверка выделения памяти
    if (new_image == NULL) {
        return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
    }
 
    struct pixel* pixels = create_pixel_array(source->width * source->height);

    //проверка выделения памяти
    if (pixels == NULL) {
        destroy_image(new_image);
        return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
    }

    //проходим по всем пикселям
    for (uint64_t row_number = 0; row_number < source->height; row_number++) {
        for (uint64_t column_number = 0; column_number < source->width; column_number++) {
            uint64_t number = row_number * source->width + column_number;
            pixels[number] = source->data[number];
        }
    }

    //проверка инициализации
    if (!init_image(new_image, source->width, source->height, pixels)) {
        destroy_pixel_array(pixels);
        destroy_image(new_image);
        return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
    }

    return (struct maybe_transformation_image) {.status=TRANSFORMATION_OK, .image=new_image};
}
