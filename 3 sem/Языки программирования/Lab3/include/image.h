#ifndef IMAGE_H
    #define IMAGE_H
    #include <stdint.h>
    #include <stdbool.h>
    #include <inttypes.h>

    struct pixel {
        uint8_t b, g, r;
    };

    struct pixel* create_pixel_array(size_t count);
    bool init_pixel(struct pixel* pixels, size_t number, uint8_t b, uint8_t g, uint8_t r);
    void destroy_pixel_array(struct pixel* pixels);

    struct image {
        uint64_t width, height;
        struct pixel* data;
    };
    
    struct image* create_image(void);
    bool init_image(struct image* image, uint64_t width, uint64_t height, struct pixel* data);
    void destroy_image(struct image* image);


    enum transformation_status{
        TRANSFORMATION_OK = 0,
        TRANSFORMATION_ERROR
    };

    struct maybe_transformation_image {
        enum transformation_status status;
        struct image* image;
    };

#endif
