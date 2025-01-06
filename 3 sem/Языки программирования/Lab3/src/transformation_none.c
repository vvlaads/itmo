#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "../include/image.h"
#include "../include/transformation_none.h"


struct maybe_transformation_image transformation_none(const struct image* source) {
    struct image* new_image = create_image();
    if (new_image == NULL) {
        return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
    }
 
    struct pixel* pixels = create_pixel_array(source->width * source->height);
    if (pixels == NULL) {
        destroy_image(new_image);
        return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
    }

    for (uint64_t row = 0; row < source->height; row++) {
        for (uint64_t i = 0; i< source->width; i++) {
            uint64_t number = row * source->width + i;
            struct pixel pixel = source->data[number];
            bool result = init_pixel(pixels, number, pixel);
            if (!result) {
                destroy_image(new_image);
                return (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
            }
        }
    }
    init_image(new_image, source->width, source->height, pixels);
    return (struct maybe_transformation_image) {.status=TRANSFORMATION_OK, .image=new_image};
}
