#ifndef OPEN_CLOSE_H
    #define OPEN_CLOSE_H
    #include <stdio.h>

    //статус открытия файла
    enum open_status {
        //успешное открытие
        OPEN_OK = 0,
        //ошибка открытия
        OPEN_ERROR
    };


    //структура для проверки открытия файла
    struct maybe_open_file {
        enum open_status status; //статус открытия файла
        FILE* file; //указатель на файл
    };


    /*пытается открыть файл с исходной картинкой
    принимает название файла
    возвращает struct maybe_open_file*/
    struct maybe_open_file open_source_file(const char* filename);


    /*пытается открыть файл с изменённой картинкой
    принимает название файла
    возвращает struct maybe_open_file*/
    struct maybe_open_file open_transformed_file(const char* filename);


    //статус закрытия файла
    enum close_status {
        //успешное закрытие
        CLOSE_OK = 0,
        //ошибка закрытия
        CLOSE_ERROR
    };
    

    /*пытается закрыть файл
    принимает указатель на файл
    возвращает статус закрытия файла*/
    enum close_status close_file(FILE* file);
#endif
