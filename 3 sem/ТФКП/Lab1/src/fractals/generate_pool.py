from PIL import Image


def generate_pool(n_iter, rgb, color, number):
    height = 1000
    width = 1000
    background = "white"
    mode = "RGB"

    image = Image.new(mode, (width, height), background)

    size = 500
    scale = size / 5

    for y in range(-size, size):
        for x in range(-size, size):
            c_x = x / scale
            c_y = y / scale
            z = complex(c_x, c_y)
            n = 0
            for n in range(n_iter):
                if z != 0:
                    z = z - (z ** number - 1) / (number * z ** (number - 1))
                    if abs(z) > 10:
                        break
                else:
                    break
            if n == n_iter - 1:
                r, g, b = color
            else:
                r = (n % 8) * 16 + rgb[0]
                g = (n % 8) * 16 + rgb[1]
                b = (n % 8) * 16 + rgb[2]
            image.putpixel((x + size, y + size), (r, g, b))

    name = "images/_pool_frac_" + str(n_iter) + ".png"
    image.save(name)
    return name
