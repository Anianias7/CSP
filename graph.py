import math

import numpy as np


from vertex import Vertex


class Graph:
    def __init__(self, number_of_vertices, constraints):
        self.constraints = constraints
        self.number_of_vertices = number_of_vertices
        self.side_length = math.floor(math.sqrt(number_of_vertices))
        self.square_matrix_of_vertices_indexes = self.square_matrix_of_vertices_indexes()
        self.list_of_vertices = []
        self.__vertices_list()

    def square_matrix_of_vertices_indexes(self):
        return np.arange(self.number_of_vertices).reshape(self.side_length, self.side_length)

    def vertex_column_num(self, vertex_num):
        return vertex_num % self.side_length

    def vertex_row_num(self, vertex_num):
        return math.floor(vertex_num / self.side_length)

    def find_vertices_num_in_row(self, row_number):
        return self.square_matrix_of_vertices_indexes[row_number]

    def find_vertices_num_in_column(self, column_number):
        return self.square_matrix_of_vertices_indexes[:, column_number]

    def __vertices_list(self):
        for i in range(self.number_of_vertices):
            self.list_of_vertices.append(Vertex(i))





