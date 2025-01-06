#ifndef TRANSFORMATION_NONE_H
    #define TRANSFORMATION_NONE_H

    /*создает копию изображения
    принимает указатель на исходное изображение
    возвращает структуру для проверки изменения*/
    struct maybe_transformation_image transformation_none(const struct image* source);
#endif
