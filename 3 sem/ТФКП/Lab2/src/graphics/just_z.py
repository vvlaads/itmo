import matplotlib.pyplot as plt

from src import checker


def create(values):
    z_good_x, z_good_y = checker.check_for_z(values)
    plt.figure()
    plt.scatter(z_good_x, z_good_y, color="green")
    return z_good_x, z_good_y
