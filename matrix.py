import numpy as np


def right_side_diagonals(matrix):
    return [np.diagonal(matrix, offset) for offset in range(-(len(matrix) - 1), len(matrix))]


def left_side_diagonals(matrix):
    return [np.diagonal(np.fliplr(matrix), offset) for offset in range(-(len(matrix) - 1), len(matrix))]


def concat_left_and_right_diagonals(matrix):
    return np.concatenate((right_side_diagonals(matrix), left_side_diagonals(matrix)))


def __filter_one_element_arrays(list_of_diagonals):
    return [diagonal for diagonal in list_of_diagonals if len(diagonal) is not 1]


def diagonals(matrix):
    return __filter_one_element_arrays(concat_left_and_right_diagonals(matrix))



