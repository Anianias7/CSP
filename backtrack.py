import numpy as np
import datetime
from heuristics import mrv_heuristic


class Backtrack:

    def __init__(self, csp_problem):
        self.csp_problem = csp_problem
        self.list_of_vertices = csp_problem.graph.list_of_vertices
        self.number_of_results = 0
        self.number_of_backs = 0
        self.time = 0

    def backtracking(self, start_vertex):
        if start_vertex is None:
            self.number_of_results += 1
            # print(np.asarray([x.variable.value for x in self.list_of_vertices]).reshape(
            #     self.csp_problem.graph.side_length, self.csp_problem.graph.side_length))
            # print("------------")
            return
        else:
            vertex = start_vertex
            domain = vertex.variable.domain
            # print(domain)
            np.random.shuffle(domain)
            for supposed_value in domain:
                vertex.variable.value = supposed_value
                is_valid = self.csp_problem.is_valid_for_entangled_variables(vertex)
                if is_valid:
                    # next_vertex = self.list_of_vertices[start_vertex.number + 1] if start_vertex.number + 1 < len(
                    #     self.list_of_vertices) else None
                    next_vertex = mrv_heuristic(self.list_of_vertices)
                    self.backtracking(next_vertex)
                self.number_of_backs += 1
            vertex.variable.value = None

    # def backtracking(self, varaible_num):
    #     if varaible_num is None:
    #         if self.number_of_results is 1:
    #             self.time = datetime.datetime.now()
    #         self.number_of_results += 1
    #         # print(np.asarray([x.variable.value for x in self.list_of_vertices]).reshape(
    #         #     self.csp_problem.graph.side_length, self.csp_problem.graph.side_length))
    #         # print("------------")
    #         return
    #     else:
    #         v = self.csp_problem.variable_list_of_vertices[varaible_num]
    #         for domain_value in self.csp_problem.list_of_variables[varaible_num].domain:
    #             vertex = self.csp_problem.variable_list_of_vertices[varaible_num][domain_value]
    #             vertex.variable.value = 1
    #             is_valid = self.csp_problem.is_valid_for_entangled_variables(vertex)
    #             if is_valid:
    #                 next_variable_num = varaible_num + 1 if varaible_num + 1 < len(
    #                     self.csp_problem.list_of_variables) else None
    #                 self.backtracking(next_variable_num)
    #             vertex.variable.value = None
    #             self.number_of_backs += 1
    #
    #
    #
    #
    #
    #
    #
# next_vertex = mcv_with_only_unassigned_neighbours_variables(self.list_of_vertices, self.csp_problem.graph.adjacency_list)
#  next_vertex = mrv_heuristic(self.list_of_vertices)
# next_vertex = mcv_heuristic(self.list_of_vertices, self.csp_problem.graph.adjacency_list)
