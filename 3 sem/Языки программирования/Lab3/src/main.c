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
    if (argc != 4) {
        fprintf(stderr, "Неверно введены аргументы\n");
        return EXIT_INVALID_ARGUMENT;
    }

    char* source_image = argv[1];
    char* transformed_image = argv[2];
    char* transformation = argv[3];

    if (check_transformation(transformation) != CHECK_TRANSFORMATION_OK) {
        fprintf(stderr, "Неверно выбран аргумент transformation\n");
        return EXIT_INVALID_ARGUMENT;
    };


    struct maybe_open_file maybe_open_source_file = open_source_file(source_image);
    if (maybe_open_source_file.status != OPEN_OK) {
        fprintf(stderr, "Не удалось открыть файл:\n");
        fprintf(stderr, "%s", source_image);
        fprintf(stderr, "\n");
        return EXIT_INPUT_OUTPUT;
    }

    struct image* image = create_image();
    if (image == NULL){
        fprintf(stderr, "Не удалось выделить память\n");
        return EXIT_OUT_OF_MEMORY;
    }

    if (from_bmp(maybe_open_source_file.file, image) != READ_OK) {
        fprintf(stderr, "Не удалось выделить память\n");
        return EXIT_OUT_OF_MEMORY;
    }

    enum close_status close_status_source_file = close_file(maybe_open_source_file.file);
    if (close_status_source_file != CLOSE_OK) {
        fprintf(stderr, "Не удалось закрыть файл:\n");
        fprintf(stderr, "%s", source_image);
        fprintf(stderr, "\n");
        return EXIT_INPUT_OUTPUT;
    }


    struct maybe_open_file maybe_open_transformed_file = open_transformed_file(transformed_image);
    if (maybe_open_transformed_file.status != OPEN_OK) {
        fprintf(stderr, "Не удалось открыть файл:\n");
        fprintf(stderr, "%s", transformed_image);
        fprintf(stderr, "\n");
        return EXIT_INPUT_OUTPUT;
    }

    enum transformation_type transformation_type = get_transformation_type(transformation);
    struct maybe_transformation_image maybe_image;
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

    destroy_image(image);

    if (maybe_image.status == TRANSFORMATION_OK) {
        if (to_bmp(maybe_open_transformed_file.file, maybe_image.image) != WRITE_OK) {
            fprintf(stderr, "Не удалось выделить память\n");
            return EXIT_OUT_OF_MEMORY;
        }
    }

    enum close_status close_status_transformed_file = close_file(maybe_open_transformed_file.file);
    if (close_status_transformed_file != CLOSE_OK) {
        fprintf(stderr, "Не удалось закрыть файл:\n");
        fprintf(stderr, "%s", transformed_image);
        fprintf(stderr, "\n");
        return EXIT_INPUT_OUTPUT;
    }
    
    return EXIT_OK;
}
