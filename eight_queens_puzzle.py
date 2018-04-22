import numpy as np

import matrix
from variable import Variable


class EightQueensPuzzle:

    def __init__(self, graph):
        self.graph = graph
        self.variable_domain = np.arange(graph.side_length)
        self.list_of_variables = []
        self.variable_list()
        self.variable_list_of_vertices = self.variable_list_of_vertices()
        self.add_domains_to_variables()
        self.adjacency_list = self.adjacency_list()
        self.add_domains_variables_in_vertices()

    def add_domains_to_variables(self):
        for variable in self.list_of_variables:
            variable.domain = self.variable_domain

    def is_valid_for_entangled_variables(self, vertex):
        adjacency_list_for_vertex = self.adjacency_list[vertex.number]
        value_from_vertex = vertex.variable.value
        return self.graph.constraints.check(
            [self.graph.list_of_vertices[i].variable.value for i in adjacency_list_for_vertex],
            value_from_vertex)

    def __find_row_neighbors_for_vertex_num(self, vertex_num):
        row_neighbors = self.graph.find_vertices_num_in_row(self.graph.vertex_row_num(vertex_num))
        return row_neighbors[np.where(row_neighbors != vertex_num)]

    def __find_column_neighbors_for_vertex_num(self, vertex_num):
        column_neighbors = self.graph.find_vertices_num_in_column(self.graph.vertex_column_num(vertex_num))
        return column_neighbors[np.where(column_neighbors != vertex_num)]

    def __find_row_columns_neighbors_indexes_for_vertex(self, vertex_num):
        return np.concatenate((self.__find_row_neighbors_for_vertex_num(vertex_num),
                               self.__find_column_neighbors_for_vertex_num(vertex_num)))

    def row_columns_adjacency_list(self):
        return [self.__find_row_columns_neighbors_indexes_for_vertex(x) for x in
                range(self.graph.number_of_vertices)]

    def all_diagonals_for_chessboard(self):
        return matrix.diagonals(self.graph.square_matrix_of_vertices_indexes)

    def find_diagonal_neighbors_for_vertex_num(self, vertex_num):
        all_diagonals = self.all_diagonals_for_chessboard()
        vertex_diagonal = sum([diagonal.tolist() for diagonal in all_diagonals if vertex_num in diagonal], [])
        return list(filter(lambda x: x != vertex_num, vertex_diagonal))

    def find_all_diagonal_neighbours_for_vertices(self):
        return [self.find_diagonal_neighbors_for_vertex_num(index) for
                index in range(self.graph.number_of_vertices)]

    def adjacency_list(self):
        return [np.concatenate((self.row_columns_adjacency_list()[vertex_num],
                                self.find_all_diagonal_neighbours_for_vertices()[vertex_num])) for vertex_num in
                range(self.graph.number_of_vertices)]

    def add_domains_variables_in_vertices(self):
        for i in range(len(self.graph.list_of_vertices)):
            self.graph.list_of_vertices[i].variable.domain = [1]

    def variable_list_of_vertices(self):
        return np.array_split(np.asarray(self.graph.list_of_vertices), self.graph.side_length)

    def variable_list(self):
        for i in range(self.graph.side_length):
            self.list_of_variables.append(Variable())
