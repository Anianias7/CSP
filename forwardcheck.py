import numpy as np
from heuristics import mrv_heuristic

class ForwardCheck:

    def __init__(self, csp_problem):
        self.latin_square = csp_problem
        self.list_of_vertices = csp_problem.graph.list_of_vertices
        self.adjacency_list = csp_problem.adjacency_list
        self.number_of_results = 0
        self.number_of_backs = 0

    def forwardchecking(self, start_vertex):
        if start_vertex is None:
            self.number_of_results += 1
            return
        else:
            vertex = start_vertex
            domain = vertex.variable.domain
            # print(domain)
            np.random.shuffle(domain)
            for supposed_value in domain:
                vertex.variable.value = supposed_value
                saved_domains = self.__save_domain(vertex)
                self.__reduce_domain(vertex)
                next_vertex = mrv_heuristic(self.list_of_vertices)
                # next_vertex = self.list_of_vertices[start_vertex.number + 1] if start_vertex.number + 1 < len(
                #     self.list_of_vertices) else None
                self.forwardchecking(next_vertex)
                self.__restore_domain(vertex, saved_domains)
                self.number_of_backs += 1
        vertex.variable.value = None

    # def forwardchecking(self, varaible_num, list_of_variables):
    #     if varaible_num is None:
    #         self.number_of_results += 1
    #         return
    #     else:
    #         for domain_value in range(len(list_of_variables[varaible_num])):
    #             vertex = list_of_variables[varaible_num][domain_value]
    #             vertex.variable.value = 1
    #
    #             saved_domains = self.__save_domain(vertex)
    #             self.__reduce_domain(vertex)
    #             # next_vertex = mrv_heuristic(self.list_of_vertices)
    #             next_variable_num = varaible_num + 1 if varaible_num + 1 < len(list_of_variables) else None
    #             self.forwardchecking(next_variable_num, self.reduce_domains_in_variables(list_of_variables))
    #             self.__restore_domain(vertex, saved_domains)
    #             self.number_of_backs += 1
    #             vertex.variable.value = None

    def __save_domain(self, vertex):
        return [self.list_of_vertices[i].variable.domain for i in self.adjacency_list[vertex.number]]

    def __restore_domain(self, vertex, saved_domain):
        for i, adjacency_no in enumerate(self.adjacency_list[vertex.number]):
            self.list_of_vertices[adjacency_no].variable.domain = saved_domain[i]

    def __reduce_domain(self, vertex):
        for i, adjacency_no in enumerate(self.adjacency_list[vertex.number]):
            self.list_of_vertices[adjacency_no].variable.domain = [value for value in
                                                                   self.list_of_vertices[adjacency_no].variable.domain
                                                                   if value != vertex.variable.value]

    def reduce_domains_in_variables(self, list_of_variables):
        return [self.filter_zero_domain_in_list(i) for i in list_of_variables]

    @staticmethod
    def filter_zero_domain_in_list(list_of_vertices):
        return [i for i in list_of_vertices if len(i.variable.domain) != 0]
