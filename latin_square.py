import numpy as np


class LatinSquare:

    def __init__(self, graph):
        self.graph = graph
        self.size = graph.side_length
        self.list_of_vertices = graph.list_of_vertices
        self.num_of_variables = graph.number_of_vertices
        self.adjacency_list = graph.adjacency_list
        self.variable_domain = np.arange(self.size)
        self.constraints = graph.constraints
        self.add_domains_to_variables()

    def add_domains_to_variables(self):
        for vertex in self.list_of_vertices:
            vertex.variable.domain = self.variable_domain

    def is_valid_for_entangled_variables(self, vertex):
        adjacency_list_for_vertex = self.adjacency_list[vertex.number]
        value_from_vertex = vertex.variable.value
        return self.constraints.check(
            [self.list_of_vertices[i].variable.value for i in adjacency_list_for_vertex],
            value_from_vertex)
