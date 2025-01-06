#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../include/bmp_converter.h"
#include "../include/image.h"


#define BM 0x4D42
#define PIXEL_BYTES 3
#define BIT_COUNT 24
#define DIB_SIZE 40

//структура заголовка bmp файла
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


//вычисляем ширину в байтах с выравниванием
static uint64_t width_with_padding(uint64_t width_in_bytes) {
    while (width_in_bytes % 4 != 0){
        width_in_bytes += 1;
    }
    return width_in_bytes;
}


//преобразуем bmp формат в структуру image
enum read_status from_bmp( FILE* in, struct image* img ) {
    struct bmp_header bmp_header; //создаем заголовок

    //проверка, что считали заголовок
    if (fread(&bmp_header, sizeof(bmp_header), 1, in) != 1) {
        return READ_INVALID_HEADER;
    };

    //проверка, что передан bmp файл
    if (bmp_header.bfType != BM) {
        return READ_INVALID_SIGNATURE;
    }

    //проверка формата в 24 бита
    if (bmp_header.biBitCount != BIT_COUNT) {
        return READ_INVALID_BITS;
    }

    uint64_t width = bmp_header.biWidth; //ширина в пикселях
    uint64_t height = bmp_header.biHeight; //высота в пикселях
    uint64_t count_pixel = width * height; //количество пикселей

    uint64_t width_in_bytes = width * PIXEL_BYTES; //ширина в байтах
    uint64_t width_in_bytes_with_padding = width_with_padding(width_in_bytes); //ширина в байтах с выравнванием
    uint64_t padding = width_in_bytes_with_padding - width_in_bytes; //размер выравнивания в байтах

    struct pixel* pixels = create_pixel_array(count_pixel); //создаем массив для пикселей

    //проходим по всем строкам
    for (uint64_t row_number = 0; row_number < height; row_number++) {
        size_t read_result = fread(&pixels[row_number*width], sizeof(struct pixel), width, in);
        if (read_result != width) {
            fprintf(stdout, "%" PRIu64 "\n", row_number);
        }
        int seek_result = fseek(in, (long) padding, SEEK_CUR);
        if (seek_result != 0) {
            return READ_INVALID_BITS;
        }
    }

    //проверка, что добавили данные в структуру image
    if (!init_image(img, width, height, pixels)) {
        destroy_pixel_array(pixels);
        destroy_image(img);
        return READ_INITIALIZATION;
    }

    return READ_OK;
}



//преобразуем структуру image в bmp формат
enum write_status to_bmp( FILE* out, struct image const* img ) {
    struct bmp_header bmp_header; //создаем заголовок

    uint64_t width = img->width; //ширина в пикселях
    uint64_t height = img->height; //высота в пикселях

    uint64_t width_in_bytes = width * PIXEL_BYTES; //ширина в байтах
    uint64_t width_in_bytes_with_padding = width_with_padding(width_in_bytes); //ширина в байтах с выравниванием
    uint64_t padding = width_in_bytes_with_padding - width_in_bytes; //размер выравнивания в байтах

    bmp_header.bfType = BM; //тип файла
    bmp_header.bfOffBits = sizeof(struct bmp_header);  //размер заголовка
    bmp_header.biWidth = (uint32_t) width; //ширина в пикселях
    bmp_header.biHeight = (uint32_t) height; //высота в пикселях
    bmp_header.biBitCount = BIT_COUNT;  //формат 24 бита
    bmp_header.biSizeImage = width_in_bytes_with_padding * height;  //размер изображения в байтах
    bmp_header.bfileSize = bmp_header.bfOffBits + bmp_header.biSizeImage; //размер файла в байтах
    bmp_header.biCompression = 0;  //без сжатия
    bmp_header.biPlanes = 1;  //число цветовых плоскостей
    bmp_header.biSize = DIB_SIZE;  //размер DIB заголовка
    bmp_header.bfReserved = 0; //зарезервированное поле
    bmp_header.biXPelsPerMeter = 0; //разрешение по горизонтали
    bmp_header.biYPelsPerMeter = 0; //разрешение по вертикали
    bmp_header.biClrUsed = 0; //количество цветов
    bmp_header.biClrImportant = 0; //количество важных цветов
    
    //проверка, что заголовок записался
    if (fwrite(&bmp_header, sizeof(struct bmp_header), 1, out)!=1) {
        return WRITE_ERROR;
    }

    //проходим по всем строкам
    for (uint64_t row_number = 0; row_number < height; row_number++) {
        uint8_t just_byte = 0;
        size_t write_result = fwrite(&img->data[row_number*width], sizeof(struct pixel), width, out);
        if (write_result != width) {
            return WRITE_ERROR;
        }
        for (size_t i = 0; i<padding; i++) {
            size_t write_padding_result = fwrite(&just_byte, sizeof(uint8_t), 1, out);
            if (write_padding_result != 1) {
                return WRITE_ERROR;
            }
        }
    }

    return WRITE_OK;
}
