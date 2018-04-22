import numpy as np


class LatinSquare:

    def __init__(self, graph):
        self.graph = graph
        self.variable_domain = np.arange(graph.side_length)
        self.add_domains_to_variables()
        self.adjacency_list = []
        self.__adjacency_list()

    def add_domains_to_variables(self):
        for vertex in self.graph.list_of_vertices:
            vertex.variable.domain = np.arange(self.graph.side_length)

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

    def __find_neighbors_indexes_for_vertex(self, vertex_num):
        return np.concatenate((self.__find_row_neighbors_for_vertex_num(vertex_num),
                               self.__find_column_neighbors_for_vertex_num(vertex_num)))

    def __adjacency_list(self):
        [self.adjacency_list.append(self.__find_neighbors_indexes_for_vertex(x)) for x in
         range(self.graph.number_of_vertices)]
