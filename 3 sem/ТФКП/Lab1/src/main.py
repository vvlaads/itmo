from tkinter import *

from fractals.generate_pool import generate_pool
import logging


def get_main_color():
    try:
        if entry_red_main.get() == "" or entry_green_main == "" or entry_blue_main == "":
            logging.info("Не выбран основной цвет")
            logging.info("Применён стандартный основной цвет")
            return 0, 0, 0
        r = int(entry_red_main.get())
        g = int(entry_green_main.get())
        b = int(entry_blue_main.get())
        if 255 >= r >= 0 and 255 >= g >= 0 and 255 >= b >= 0:
            return r, g, b
        else:
            return 0, 0, 0
    except ValueError:
        logging.warning("Неверно введён основной цвет")
        logging.info("Применён стандартный основной цвет")
        return 0, 0, 0


def get_color():
    try:
        if entry_red.get() == "" or entry_green == "" or entry_blue == "":
            logging.info("Не выбрана цветовая схема")
            logging.info("Применена стандартная цветовая схема")
            return 128, 64, 128
        r = int(entry_red.get())
        g = int(entry_green.get())
        b = int(entry_blue.get())
        if 255 >= r >= 0 and 255 >= g >= 0 and 255 >= b >= 0:
            return r, g, b
        else:
            return 128, 64, 128
    except ValueError:
        logging.warning("Неверно введена цветовая схема")
        logging.info("Применена стандартная цветовая схема")
        return 128, 64, 128


def get_number():
    try:
        if entry_number.get() == "":
            logging.info("Не выбрано число N")
            logging.info("Применено стандартное N = 2")
            return 2
        number = int(entry_number.get())
        if 10 >= number >= 2:
            return number
        else:
            return 2
    except ValueError:
        logging.warning("Не удалось преобразовать")
        logging.info("Применено стандартное N = 2")
        return 2


def click():
    try:
        num = int(entry_iter.get())
        if 1 <= num <= 100:
            new_name = generate_pool(num, get_color(), get_main_color(), get_number())
            new_img = PhotoImage(file=new_name)
            image.configure(image=new_img)
            image.image = new_img
    except ValueError:
        logging.warning("Неверно введено число итераций")


logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
window = Tk()
window.geometry('800x600')
window.title("Бассейн Ньютона")

label_name = Label(window, text="Фрактал: Бассейн Ньютона")
label_name.grid(row=0, column=0, columnspan=3)

label_func = Label(window, text="Функция: z_(n+1) = z_n + (z_n ^ N - 1)/(N * z_n ^ (N - 1))")
label_func.grid(row=1, column=0, columnspan=3)

label_entry_iter = Label(window, text="Введите количество итераций:")
label_entry_iter.grid(row=2, column=0, columnspan=2)
entry_iter = Entry(window)
entry_iter.grid(row=2, column=2)

label_number = Label(window, text="Введите число N от 2 до 10 (необязательно): ")
label_number.grid(row=3, column=0, columnspan=2)
entry_number = Entry(window)
entry_number.grid(row=3, column=2)

button = Button(window, text="Сгенерировать изображение", command=click)
button.grid(row=4, column=0, ipadx=100, ipady=20, columnspan=3)

label_color = Label(window, text="Цветовая схема (необязательно):")
label_color.grid(row=5, column=0, columnspan=3, pady=(50, 0))

label_red = Label(window, text="red (от 0 до 255):")
label_red.grid(row=6, column=0)
label_green = Label(window, text="green (от 0 до 255):")
label_green.grid(row=6, column=1)
label_blue = Label(window, text="blue (от 0 до 255):")
label_blue.grid(row=6, column=2)

entry_red = Entry(window)
entry_red.grid(row=7, column=0)
entry_green = Entry(window)
entry_green.grid(row=7, column=1)
entry_blue = Entry(window)
entry_blue.grid(row=7, column=2)

label_color_main = Label(window, text="Основной цвет (необязательно):")
label_color_main.grid(row=8, column=0, columnspan=3)

label_red_main = Label(window, text="red (от 0 до 255):")
label_red_main.grid(row=9, column=0)
label_green_main = Label(window, text="green (от 0 до 255):")
label_green_main.grid(row=9, column=1)
label_blue_main = Label(window, text="blue (от 0 до 255):")
label_blue_main.grid(row=9, column=2)

entry_red_main = Entry(window)
entry_red_main.grid(row=10, column=0)
entry_green_main = Entry(window)
entry_green_main.grid(row=10, column=1)
entry_blue_main = Entry(window)
entry_blue_main.grid(row=10, column=2)

image = Label(window)
image.grid(row=0, column=3, rowspan=12, padx=(50, 20), pady=(20, 20))

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)
window.rowconfigure(9, weight=1)
window.rowconfigure(10, weight=1)
window.rowconfigure(11, weight=2)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=5)
window.mainloop()
