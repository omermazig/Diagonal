def print_array(array):
    for i in array:
        print(i)
    print('\r\n')


def create_diagonals_array(size):
    array = [[[0] * size] * size]
    print_array(array)
    row = 0
    for column in range(size):
        array[column][row] = 1
        array[size - column][row] = 1
        row += 1
    print_array(array)
    return array


print_array(create_diagonals_array(3))
