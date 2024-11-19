import numpy as np
import matplotlib.pyplot as plt


def func(x_value, y_value):
    return x_value ** 3 * y_value ** 2 * (4 - x_value - y_value)


def make_data_for_surface():
    array_x = np.linspace(-5, 5, 300)
    array_y = np.linspace(-5, 5, 300)
    xgrid, ygrid = np.meshgrid(array_x, array_y)
    zgrid = func(xgrid, ygrid)
    return xgrid, ygrid, zgrid


def make_data_for_point_a():
    array_x = np.zeros(20)
    array_y = np.linspace(-5, 5, 20)
    xgrid, ygrid = np.meshgrid(array_x, array_y)
    zgrid = func(xgrid, ygrid)
    return xgrid, ygrid, zgrid


def make_data_for_point_b():
    array_x = np.linspace(-5, 5, 20)
    array_y = np.zeros(20)
    xgrid, ygrid = np.meshgrid(array_x, array_y)
    zgrid = func(xgrid, ygrid)
    return xgrid, ygrid, zgrid


def make_data_for_point_c():
    array_x = [2]
    array_y = [4 / 3]
    xgrid, ygrid = np.meshgrid(array_x, array_y)
    zgrid = func(xgrid, ygrid)
    return xgrid, ygrid, zgrid


fig = plt.figure(figsize=(16, 9))
ax_3d = fig.add_subplot(1, 2, 1, projection='3d')
ax_2d = fig.add_subplot(1, 2, 2)

ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

ax_3d.set_xlim(-5, 5)
ax_3d.set_ylim(-5, 5)
ax_3d.set_zlim(0, 5)

x, y, z = make_data_for_surface()
ax_3d.plot_wireframe(x, y, z, color="#7fc7ff")
c1 = ax_2d.contour(x, y, z, np.linspace(-10, 10, 10))
plt.clabel(c1)

x, y, z = make_data_for_point_a()
ax_3d.scatter(x, y, z, color="#f80000")
ax_2d.scatter(x, y, color="#f80000")

x, y, z = make_data_for_point_b()
ax_3d.scatter(x, y, z, color="#f80000")
ax_2d.scatter(x, y, color="#f80000")

x, y, z = make_data_for_point_c()
ax_3d.scatter(x, y, z, color="#f80000")
ax_2d.scatter(x, y, color="#f80000")

plt.show()
