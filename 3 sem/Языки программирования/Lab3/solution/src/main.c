#include <inttypes.h>
#include <stdio.h>

#include "../include/bmp_converter.h"
#include "../include/image.h"
#include "../include/open_close.h"
#include "../include/transformation_none.h"
#include "../include/util.h"


#define EXIT_OK 0
#define EXIT_ERROR 1
#define EXIT_INPUT_OUTPUT 5
#define EXIT_OUT_OF_MEMORY 12
#define EXIT_INVALID_ARGUMENT 22


int main( int argc, char** argv ) {

    //проверка на количество аргументов в команде
    if (argc != 4) {
        fprintf(stderr, "Неверно введены аргументы\n");
        return EXIT_INVALID_ARGUMENT;
    }

    char* source_image = argv[1]; //адрес исходного файла
    char* transformed_image = argv[2]; //адрес файла, в который записываем
    char* transformation = argv[3]; //тип преобразования

    //проверка типа преобразования
    if (check_transformation(transformation) != CHECK_TRANSFORMATION_OK) {
        fprintf(stderr, "Неверно выбран аргумент transformation\n");
        return EXIT_INVALID_ARGUMENT;
    };

    //открываем исходный файл
    struct maybe_open_file maybe_open_source_file = open_source_file(source_image);
    if (maybe_open_source_file.status != OPEN_OK) {
        fprintf(stderr, "Не удалось открыть файл:\n%s\n", source_image);
        return EXIT_INPUT_OUTPUT;
    }

    //создаем структуру image
    struct image* image = create_image();
    if (image == NULL){
        fprintf(stderr, "Не удалось выделить память\n");
        return EXIT_OUT_OF_MEMORY;
    }

    //пытаемся преобразовать исходный bmp в image
    switch (from_bmp(maybe_open_source_file.file, image)) {
        case READ_OK: {
            break;
        }
        case READ_INVALID_HEADER: {
            fprintf(stderr, "Ошибка чтения заголовка\n");
            return EXIT_INPUT_OUTPUT;
        }
        case READ_INVALID_BITS: {
            fprintf(stderr, "Ошибка чтения данных изображения\n");
            return EXIT_INPUT_OUTPUT;
        }
        case READ_INVALID_SIGNATURE: {
            fprintf(stderr, "Ошибка формата файла\n");
            return EXIT_INPUT_OUTPUT;
        }
        case READ_OUT_OF_MEMORY: {
            fprintf(stderr, "Ошибка выделения памяти\n");
            return EXIT_OUT_OF_MEMORY;
        }
        case READ_INITIALIZATION: {
            fprintf(stderr, "Ошибка инициализации\n");
            return EXIT_ERROR;
        }
        default: {
            fprintf(stderr, "Ошибка при чтении файла\n");
            return EXIT_ERROR;
        }
    }

    //закрываем исходный файл
    enum close_status close_status_source_file = close_file(maybe_open_source_file.file);
    if (close_status_source_file != CLOSE_OK) {
        fprintf(stderr, "Не удалось закрыть файл:\n%s\n", source_image);
        return EXIT_INPUT_OUTPUT;
    }

    //открываем файл для записи
    struct maybe_open_file maybe_open_transformed_file = open_transformed_file(transformed_image);
    if (maybe_open_transformed_file.status != OPEN_OK) {
        fprintf(stderr, "Не удалось открыть файл:\n%s\n", transformed_image);
        return EXIT_INPUT_OUTPUT;
    }

    //получаем тип преобразования
    enum transformation_type transformation_type = get_transformation_type(transformation);
    struct maybe_transformation_image maybe_image;

    //выполняем преобразование
    switch (transformation_type) {
        case TRANSFORMATION_TYPE_NONE: {
            maybe_image = transformation_none(image);
            break;
        }
        default: {
            maybe_image = (struct maybe_transformation_image) {.status=TRANSFORMATION_ERROR};
            break;
        }
    }

    destroy_image(image); //очистка памяти от исходного image

    //если преобразование успешно, то записываем в файл
    if (maybe_image.status == TRANSFORMATION_OK) {
        if (to_bmp(maybe_open_transformed_file.file, maybe_image.image) != WRITE_OK) {
            fprintf(stderr, "Не удалось выделить память\n");
            return EXIT_OUT_OF_MEMORY;
        }
    }

    //закрываем файл для записи
    enum close_status close_status_transformed_file = close_file(maybe_open_transformed_file.file);
    if (close_status_transformed_file != CLOSE_OK) {
        fprintf(stderr, "Не удалось закрыть файл:\n%s\n", transformed_image);
        return EXIT_INPUT_OUTPUT;
    }
    
    return EXIT_OK;
}
