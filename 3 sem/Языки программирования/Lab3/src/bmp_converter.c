#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../include/bmp_converter.h"
#include "../include/image.h"
#include "../include/util.h"


#define BM 0x4D42
#define PIXEL_BYTES 3

#pragma pack(push, 1)
struct bmp_header 
{
        uint16_t bfType;
        uint32_t bfileSize;
        uint32_t bfReserved;
        uint32_t bfOffBits;
        uint32_t biSize;
        uint32_t biWidth;
        uint32_t biHeight;
        uint16_t biPlanes;
        uint16_t biBitCount;
        uint32_t biCompression;
        uint32_t biSizeImage;
        uint32_t biXPelsPerMeter;
        uint32_t biYPelsPerMeter;
        uint32_t biClrUsed;
        uint32_t biClrImportant;
};
#pragma pack(pop)


enum read_status from_bmp( FILE* in, struct image* img ) {
    struct bmp_header bmp_header;
    if (fread(&bmp_header, sizeof(bmp_header), 1, in) != 1) {
        return READ_INVALID_HEADER;
    };

    if (bmp_header.bfType != BM) {
        return READ_INVALID_SIGNATURE;
    }

    if (bmp_header.biBitCount != 24) {
        return READ_INVALID_BITS;
    }

    uint32_t width = bmp_header.biWidth;
    uint32_t height = bmp_header.biHeight;
    uint32_t count_pixel = width * height;

    uint64_t width_with_padding = width * PIXEL_BYTES;
    width_with_padding = padding(width_with_padding);

    fseek(in, (long) bmp_header.bfOffBits, SEEK_SET);


    struct pixel* pixels = create_pixel_array(count_pixel);
    
    for (uint32_t row = 0; row < height; row++) {
        uint8_t* row_data = malloc(width_with_padding);
        if (row_data == NULL){
            destroy_pixel_array(pixels);
            return READ_OUT_OF_MEMORY;
        }

        fread(row_data, width_with_padding, 1, in);
        for (uint64_t i = 0; i < width * PIXEL_BYTES; i += 3) {
            uint8_t b = row_data[i];
            uint8_t g = row_data[i+1];
            uint8_t r = row_data[i+2];
            init_pixel(pixels, (row*width) + (i / 3), b, g, r);
        }
        free(row_data);
    }

    if (!init_image(img, width, height, pixels)) {
        destroy_pixel_array(pixels);
        destroy_image(img);
        return READ_OUT_OF_MEMORY;
    }

    return READ_OK;
}


enum write_status to_bmp( FILE* out, struct image const* img ) {
    struct bmp_header bmp_header;

    uint32_t width_with_padding = img->width * PIXEL_BYTES;
    width_with_padding = padding(width_with_padding);
    uint32_t padding = width_with_padding - img->width * PIXEL_BYTES;

    bmp_header.bfType = BM;
    bmp_header.bfReserved = 0;
    bmp_header.bfOffBits = sizeof(struct bmp_header);  // Размер заголовка
    bmp_header.biSize = 40;  // Размер DIB заголовка
    bmp_header.biWidth = (uint32_t) img->width;
    bmp_header.biHeight = (uint32_t) img->height;
    bmp_header.biPlanes = 1;  // Один канал для изображения
    bmp_header.biBitCount = 24;  // 24 бита
    bmp_header.biCompression = 0;  // Без сжатия
    bmp_header.biSizeImage = width_with_padding * img->height;  // Размер изображения в байтах
    bmp_header.biXPelsPerMeter = 0;
    bmp_header.biYPelsPerMeter = 0;
    bmp_header.biClrUsed = 0;
    bmp_header.biClrImportant = 0;
    bmp_header.bfileSize = bmp_header.bfOffBits + bmp_header.biSizeImage;

    fwrite(&bmp_header, sizeof(struct bmp_header), 1, out);
    printf("%" PRIu64 "\n", img->width * PIXEL_BYTES);
    printf("%" PRIu32 "\n", width_with_padding);
    printf("%" PRIu32 "\n", padding);

    for (uint64_t row = 0; row < img->height; row++) {
        uint8_t* row_data = malloc(width_with_padding);
        if (row_data == NULL) {
            return WRITE_OUT_OF_MEMORY;
        }

        memset(row_data, 0, width_with_padding);

        for (uint32_t i = 0; i < img->width; i++) {
            uint64_t number = row * img->width + i;
            row_data[i * 3] = img->data[number].b;
            row_data[i * 3 + 1] = img->data[number].g;
            row_data[i * 3 + 2] = img->data[number].r;
        }

        fwrite(row_data, width_with_padding, 1, out);
        free(row_data);
    }


    return WRITE_OK;
}
