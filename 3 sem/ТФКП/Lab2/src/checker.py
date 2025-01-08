def check_for_z(array):
    good_x_array = []
    good_y_array = []
    for i in range(len(array)):
        for j in range(len(array)):
            if not ((array[i] == 0 and 0 <= array[j] <= 1) or (array[j] <= 0)):
                good_x_array.append(array[i])
                good_y_array.append(array[j])
    return good_x_array, good_y_array
