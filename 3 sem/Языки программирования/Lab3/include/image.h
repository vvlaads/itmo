#ifndef IMAGE_H
    #define IMAGE_H
    #include <stdint.h>
    #include <stdbool.h>
    #include <inttypes.h>

    //структура пикселя
    struct pixel {
        uint8_t b; //синий цвет
        uint8_t g; //зелёный цвет
        uint8_t r; //красный цвет
    };


    /*выделение динамической памяти для массива пикселей
    принимает количество пикселей
    возвращает массив пикселей*/
    struct pixel* create_pixel_array(size_t count);


    /*освобождает динамическую память от массива
    принимает массив пикселей*/
    void destroy_pixel_array(struct pixel* pixels);


    //стуктура изображения
    struct image {
        uint64_t width; //ширина изображения
        uint64_t height; //высота изображения
        struct pixel* data; //массив пикселей
    };
    

    /*выделение динамической памяти для изображения
    возвращает указатель на изображение*/
    struct image* create_image(void);


    /*инициализирует изображение
    принимает указатель на изображение, ширина изображения, высота изображения, массив пикселей
    возвращает булевое значение*/
    bool init_image(struct image* image, uint64_t width, uint64_t height, struct pixel* data);


    /*освобождает динамическую память от изображения
    принимает указатель на изображение*/
    void destroy_image(struct image* image);


    //статус изменения
    enum transformation_status{
        //изменение успешно
        TRANSFORMATION_OK = 0,
        //ошибка изменения
        TRANSFORMATION_ERROR
    };


    //структура для проверки изменения
    struct maybe_transformation_image {
        enum transformation_status status; //статус изменения
        struct image* image; //указатель на изображение
    };
#endif
