import matplotlib.pyplot as plt
from src.functions import *


def create(z_good_x, z_good_y, func):
    w_good_x = []
    w_good_y = []
    generate_after_func(z_good_x, z_good_y, w_good_x, w_good_y, func)

    plt.figure()
    plt.scatter(w_good_x, w_good_y, color="green")
    plt.xlim(max(-2, min(w_good_x)), min(2, max(w_good_x)))
    plt.ylim(max(-2, min(w_good_y)), min(2, max(w_good_y)))
    return w_good_x, w_good_y
