import math

import numpy as np

from vertex import Vertex


class Graph:
    def __init__(self, number_of_vertices, constraints):
        self.constraints = constraints
        self.number_of_vertices = number_of_vertices
        self.side_length = math.floor(math.sqrt(number_of_vertices))
        self.adjacency_list = []
        self.square_matrix_of_vertices_indexes = self.__square_matrix_of_vertices_indexes()
        self.__adjacency_list()
        self.list_of_vertices = []
        self.__vertices_list()

    def __square_matrix_of_vertices_indexes(self):
        return np.arange(self.number_of_vertices).reshape(self.side_length, self.side_length)

    def __vertex_column_num(self, vertex_num):
        return vertex_num % self.side_length

    def __vertex_row_num(self, vertex_num):
        return math.floor(vertex_num / self.side_length)

    def __find_vertices_num_in_row(self, row_number):
        return self.square_matrix_of_vertices_indexes[row_number]

    def __find_vertices_num_in_column(self, column_number):
        return self.square_matrix_of_vertices_indexes[:, column_number]

    def __find_row_neighbors_for_vertex_num(self, vertex_num):
        row_neighbors = self.__find_vertices_num_in_row(self.__vertex_row_num(vertex_num))
        return row_neighbors[np.where(row_neighbors != vertex_num)]

    def __find_column_neighbors_for_vertex_num(self, vertex_num):
        column_neighbors = self.__find_vertices_num_in_column(self.__vertex_column_num(vertex_num))
        return column_neighbors[np.where(column_neighbors != vertex_num)]

    def __find_neighbors_for_vertex(self, vertex_num):
        return np.concatenate((self.__find_row_neighbors_for_vertex_num(vertex_num),
                               self.__find_column_neighbors_for_vertex_num(vertex_num)))

    def __adjacency_list(self):
        [self.adjacency_list.append(self.__find_neighbors_for_vertex(x)) for x in range(self.number_of_vertices)]

    def __vertices_list(self):
        for i in range(self.number_of_vertices):
            self.list_of_vertices.append(Vertex(i))
