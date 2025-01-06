#ifndef BMP_CONVERTER_H
    #define BMP_CONVERTER_H
    #include <stdio.h>
    #include <stdlib.h>
    #include <stdint.h>
    #include <inttypes.h>
    
    #include "../include/image.h"

    //статус чтения файла
    enum read_status {
        //чтение усешно
        READ_OK = 0,
        //некорректный тип файла
        READ_INVALID_SIGNATURE,
        //некорректные данные изображения
        READ_INVALID_BITS,
        //некорректные данные заголовка
        READ_INVALID_HEADER,
        //нехватка памяти
        READ_OUT_OF_MEMORY,
        //ошибка инициализации
        READ_INITIALIZATION,
        //ошибка чтения
        READ_ERROR
    };


    /*преобразовывает bmp файл в struct image
    принимает указатель на файл, изображение
    возвращает статус чтения файла*/
    enum read_status from_bmp( FILE* in, struct image* img );


    //статус записи в файл
    enum  write_status {
        //запись успешна
        WRITE_OK = 0,
        //ошибка записи
        WRITE_ERROR,
        //нехватка памяти
        WRITE_OUT_OF_MEMORY
    };
    

    /*преобразовывает struct image в bmp файл
    принимает указатель на файл, изображение
    возвращает статус записи в файл*/
    enum write_status to_bmp( FILE* out, struct image const* img ); 
#endif
