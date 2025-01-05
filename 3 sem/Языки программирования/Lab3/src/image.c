#include <stdint.h>
#include <stdlib.h>

#include "../include/image.h"


struct pixel* create_pixel_array(size_t count) {
    struct pixel* pixels = malloc(sizeof(struct pixel) * count);
    if (pixels != NULL) {
        return pixels;
    }
    return NULL;
}


bool init_pixel(struct pixel* pixels, size_t number, uint8_t b, uint8_t g, uint8_t r) {
    if (pixels != NULL) {
        pixels[number].b = b;
        pixels[number].g = g;
        pixels[number].r = r;
        return true;
    }
    return false;
}


void destroy_pixel_array(struct pixel* pixels) {
    if (pixels != NULL) free(pixels);
}


struct image* create_image(void) {
    struct image* new_image = malloc(sizeof(struct image));
    if (new_image != NULL) {
        return new_image;
    }
    return NULL;
}


bool init_image(struct image* image, uint64_t width, uint64_t height, struct pixel* data){
    if (image != NULL) {
        image->width = width;
        image->height = height;
        image->data = data;
        return true;
    }
    return false;
}


void destroy_image(struct image* image) {
    if (image != NULL) free(image);
}
