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

    struct pixel* pixels = create_pixel_array(count_pixel); //создаем массив для пикселей
    
    uint8_t* row_data = malloc(width_in_bytes_with_padding); //массив байтов для одной строки

    //выходим, если не смогли выделить память
    if (row_data == NULL){
        destroy_pixel_array(pixels);
        return READ_OUT_OF_MEMORY;
    }

    //проходим по всем строкам
    for (uint64_t row_number = 0; row_number < height; row_number++) {
        //проверка, что считали строку
        size_t test = fread(row_data, width_in_bytes_with_padding, 1, in);

        if (test != 1) {
            if (feof(in)) {
            fprintf(stdout,"Достигнут конец файла\n");
            fprintf(stdout, "%" PRIu64 "\n", row_number);
            fprintf(stdout, "Ширина: %" PRIu64 "\n", width);
            fprintf(stdout, "Ширина байт: %" PRIu64 "\n", width_in_bytes);
            fprintf(stdout, "Ширина байт + оступ: %" PRIu64 "\n", width_in_bytes_with_padding);
            fprintf(stdout, "Высота: %" PRIu64 "\n", height);
            fprintf(stdout, "Размер: %" PRIu32 "\n", bmp_header.biSizeImage);
            fseek(in, 0, SEEK_END);
            long end_pos = ftell(in);
            printf("Позиция в конце файла: %ld\n", end_pos);
            //return READ_INITIALIZATION;
            }
            fprintf(stdout, "fi");
            //return READ_INITIALIZATION;
        };
  
        //проходим по байтам из строки, содержащим полезную информацию
        for (uint64_t byte_number = 0; byte_number < width_in_bytes; byte_number += 3) {
            uint8_t b = row_data[byte_number];
            uint8_t g = row_data[byte_number+1];
            uint8_t r = row_data[byte_number+2];
            struct pixel pixel = (struct pixel) {.b = b, .g = g, .r = r};

            //проверка, что добавили пиксель в массив
            if (!init_pixel(pixels, (row_number * width) + (byte_number / 3), pixel)) {
                fprintf(stdout, "se");
                free(row_data);
                return READ_INITIALIZATION;
            }
        }
    }

    free(row_data); //очищаем память

    //проверка, что добавили данные в структуру image
    if (!init_image(img, width, height, pixels)) {
        destroy_pixel_array(pixels);
        destroy_image(img);
        fprintf(stdout, "th");
        return READ_INITIALIZATION;
    }

    return READ_OK;
}



//преобразуем структуру image в bmp формат
enum write_status to_bmp( FILE* out, struct image const* img ) {
    printf("sdfsf");
    struct bmp_header bmp_header; //создаем заголовок

    uint64_t width = img->width; //ширина в пикселях
    uint64_t height = img->height; //высота в пикселях
    uint64_t width_in_bytes = width * PIXEL_BYTES; //ширина в байтах

    uint64_t width_in_bytes_with_padding = width_with_padding(width_in_bytes); //ширина в байтах с выравниванием

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

    uint8_t* row_data = malloc(width_in_bytes_with_padding); //массив байтов для одной строки

    //выходим, если не смогли выделить память
    if (row_data == NULL) {
        return WRITE_OUT_OF_MEMORY;
    }

    memset(row_data, 0, width_in_bytes_with_padding); //заполняем нулями

    //проходим по всем строкам
    for (uint64_t row_number = 0; row_number < height; row_number++) {

        // //проходим по пикселям в строке
        for (uint64_t pixel_number = 0; pixel_number < width; pixel_number++) {
            uint64_t number = row_number * width + pixel_number;
            row_data[pixel_number * 3] = img->data[number].b;
            row_data[pixel_number * 3 + 1] = img->data[number].g;
            row_data[pixel_number * 3 + 2] = img->data[number].r;
        }

        //проверка, что данные записались
        if (fwrite(row_data, width_in_bytes_with_padding, 1, out) != 1) {
            free(row_data);
            return WRITE_ERROR;
        }
    }

    free(row_data); //освобождаем память

    return WRITE_OK;
}
