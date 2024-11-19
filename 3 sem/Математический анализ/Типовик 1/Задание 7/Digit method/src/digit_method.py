import time


def z(x, y):
    return x ** 3 * y ** 2 * (4 - x - y)


def grad_x(x, y):
    return 3 * x ** 2 * y ** 2 * (4 - x - y) - x ** 3 * y ** 2


def grad_y(x, y):
    return 2 * x ** 3 * y * (4 - x - y) - x ** 3 * y ** 2


class Check:
    def __init__(self, start_x, start_y, epsilon, delta, array_x, array_y):
        self.break_point = None
        self.point = None
        self.value = None
        self.time = None
        self.iter = None
        self.start_x = start_x
        self.start_y = start_y
        self.epsilon = epsilon
        self.delta = delta
        self.array_x = array_x
        self.array_y = array_y

    def get_point(self):
        return self.point

    def get_time(self):
        return self.time

    def get_value(self):
        return self.value

    def get_iter(self):
        return self.iter

    def get_break_point(self):
        return self.break_point

    def get_array_x(self):
        return self.array_x

    def get_array_y(self):
        return self.array_y

    def check(self):
        time_start = time.time()
        count = 0
        x_extr = 2
        y_extr = 4 / 3
        z_extr = z(x_extr, y_extr)
        x0 = self.start_x
        y0 = self.start_y
        while True:
            count += 1
            a_k = 1
            self.array_x.append(x0)
            self.array_y.append(y0)
            z0 = z(x0, y0)
            delta_z = z_extr - z0
            delta_x = x_extr - x0
            delta_y = y_extr - y0
            x1 = grad_x(x0, y0)
            y1 = grad_y(x0, y0)
            while ((a_k * x1) ** 2 + (a_k * y1) ** 2) > delta_x * delta_x + delta_y * delta_y:
                a_k = a_k / 2

            if abs(delta_z) < self.epsilon:
                self.break_point = "|delta_z| < epsilon"
                self.iter = count
                self.point = x0, y0
                self.value = z0
                self.time = (time.time() - time_start)
                break

            if (delta_x * delta_x + delta_y * delta_y) < self.delta * self.delta:
                self.break_point = "||delta_x, delta_y|| < delta"
                self.iter = count
                self.point = x0, y0
                self.value = z0
                self.time = (time.time() - time_start)
                break

            if count > 100:
                self.break_point = "Превышено число итераций = 100"
                self.iter = count
                self.point = x0, y0
                self.value = z0
                self.time = (time.time() - time_start)
                break

            x0 = x0 + a_k * x1
            y0 = y0 + a_k * y1
