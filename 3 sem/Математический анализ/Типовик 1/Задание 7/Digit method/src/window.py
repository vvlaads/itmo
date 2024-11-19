import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

from digit_method import Check


def func(x_value, y_value):
    return x_value ** 3 * y_value ** 2 * (4 - x_value - y_value)


def click():
    try:
        start_x = float(entry_x.get())
        start_y = float(entry_y.get())
        epsilon = float(entry_epsilon.get())
        delta = float(entry_delta.get())
        array_x = []
        array_y = []
        if 4 - start_y > start_x > 0 and 4 > start_y > 0 and epsilon > 0 and delta > 0:
            check = Check(start_x, start_y, epsilon, delta, array_x, array_y)
            check.check()
            array_x = check.get_array_x()
            array_y = check.get_array_y()
            value = check.get_value()
            iter_num = check.get_iter()
            time = check.get_time()
            break_point = check.get_break_point()
            point = check.get_point()

            for label in window.grid_slaves():
                if int(label.grid_info()["column"]) == 1:
                    if int(label.grid_info()["row"]) == 3:
                        label.configure(text=break_point)
                        label.text = break_point
                    elif int(label.grid_info()["row"]) == 4:
                        label.configure(text=iter_num)
                        label.text = iter_num
                    elif int(label.grid_info()["row"]) == 5:
                        label.configure(text="{}".format(point))
                        label.text = "{}".format(point)
                    elif int(label.grid_info()["row"]) == 6:
                        label.configure(text=value)
                        label.text = value
                    elif int(label.grid_info()["row"]) == 7:
                        label.configure(text=str(time) + " сек")
                        label.text = str(time) + " сек"

            fig = plt.figure(figsize=(8, 6))

            # ax_3d = fig.add_subplot(projection='3d')
            # ax_3d.set_xlabel('x')
            # ax_3d.set_ylabel('y')
            # ax_3d.set_zlabel('z')
            x, y, z = make_data_for_surface()
            #
            # ax_3d.set_xlim(-5, 5)
            # ax_3d.set_ylim(-5, 5)
            # ax_3d.set_zlim(0, 5)
            # ax_3d.plot_wireframe(x, y, z, color="#7fc7ff")
            # x, y, z = make_data_for_scatter(array_x, array_y)
            # ax_3d.scatter(x, y, z, color="#f80000")

            ax_2d = fig.add_subplot()
            ax_2d.set_xlabel('x')
            ax_2d.set_ylabel('y')
            c1 = ax_2d.contour(x, y, z, np.linspace(-10, 10, 10))
            plt.clabel(c1)
            x, y, z = make_data_for_scatter(array_x, array_y)

            ax_2d.plot(x, y, color='k', marker='o', markerfacecolor='r')

            plt.show()
    except ValueError:
        print("Не удалось преобразовать")


def make_data_for_surface():
    array_x = np.linspace(-1, 4, 100)
    array_y = np.linspace(-1, 4, 100)
    xgrid, ygrid = np.meshgrid(array_x, array_y)
    zgrid = func(xgrid, ygrid)
    return xgrid, ygrid, zgrid


def make_data_for_scatter(array_x, array_y):
    array_z = []
    for i in range(len(array_x)):
        array_z.append(func(array_x[i], array_y[i]))
    return array_x, array_y, array_z


window = Tk()
window.geometry('800x600')

label_x = Label(window, text="Начальный x:")
label_x.grid(row=0, column=0)

entry_x = Entry(window)
entry_x.grid(row=0, column=1, ipady=10)

label_y = Label(window, text="Начальный y:")
label_y.grid(row=0, column=2)

entry_y = Entry(window)
entry_y.grid(row=0, column=3, ipady=10)

label_x = Label(window, text="Значение epsilon:")
label_x.grid(row=1, column=0)

entry_epsilon = Entry(window)
entry_epsilon.grid(row=1, column=1, ipady=10)

label_y = Label(window, text="Значение delta:")
label_y.grid(row=1, column=2)

entry_delta = Entry(window)
entry_delta.grid(row=1, column=3, ipady=10)

button = Button(window, text="Вычислить", command=click)
button.grid(row=2, column=0, columnspan=4, ipadx=200, ipady=20)

label_break = Label(window, text="Критерий остановки:")
label_break.grid(row=3, column=0)

label_break_descr = Label(window, text="")
label_break_descr.grid(row=3, column=1)

label_iter = Label(window, text="Число итераций:")
label_iter.grid(row=4, column=0)

label_iter = Label(window, text="")
label_iter.grid(row=4, column=1)

label_point = Label(window, text="Полученная точка:")
label_point.grid(row=5, column=0)

label_point = Label(window, text="")
label_point.grid(row=5, column=1)

label_value = Label(window, text="Значение функции:")
label_value.grid(row=6, column=0)

label_value = Label(window, text="")
label_value.grid(row=6, column=1)

label_time = Label(window, text="Время выполнения:")
label_time.grid(row=7, column=0)

label_time = Label(window, text="")
label_time.grid(row=7, column=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=2)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=2)
window.mainloop()
