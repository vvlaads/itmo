import numpy as np
import matplotlib.pyplot as plt

from graphics import just_z, func_z
from functions import *


def generate_array(min_, max_, multiplier):
    step = 1 / multiplier
    array = np.arange(min_ * multiplier, (max_ + step) * multiplier, step * multiplier)
    return array / multiplier


values = generate_array(-2, 2, 20)
z_good_x, z_good_y = just_z.create(values)

w1_good_x, w1_good_y = func_z.create(z_good_x, z_good_y, func_w1)
w2_good_x, w2_good_y = func_z.create(w1_good_x, w1_good_y, func_w2)
w3_good_x, w3_good_y = func_z.create(w2_good_x, w2_good_y, func_w3)
w4_good_x, w4_good_y = func_z.create(w3_good_x, w3_good_y, func_w4)
w_good_x, w_good_y = func_z.create(w4_good_x, w4_good_y, func_w)

plt.show()
