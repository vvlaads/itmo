#ifndef UTIL_H
    #define UTIL_H
    #include <string.h>
    #include <inttypes.h>

    //статус проверки типа преобразования
    enum check_transformation_status {
        //тип корректен
        CHECK_TRANSFORMATION_OK = 0,
        //тип некорректен
        CHECK_TRANSFORMATION_ERROR
    };
    

    /*проверяет корректность типа преобразования
    принимает название типа преобразования
    возвращает статус проверки типа преобразования*/
    enum check_transformation_status check_transformation(char* message);


    //тип преобразования
    enum transformation_type {
        //без изменений
        TRANSFORMATION_TYPE_NONE = 0,
        //поворот на 90 градусов по часовой стрелке
        TRANSFORMATION_TYPE_CW90,
        //поворот на 90 градусов против часовой стрелке
        TRANSFORMATION_TYPE_CCW90,
        //отражение по горизонтали
        TRANSFORMATION_TYPE_FLIPH,
        //отражение по вертикали
        TRANSFORMATION_TYPE_FLIPV,
        //ошибка типа преобразования
        TRANSFORMATION_TYPE_ERROR
    };


    /*определяет тип преобразования
    принимает названиетипа преобразования
    возвращает тип преобразования*/
    enum transformation_type get_transformation_type(char* message);
#endif
