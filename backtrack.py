from heuristics import mrv_heuristic


class Backtrack:

    def __init__(self, csp_problem):
        self.csp_problem = csp_problem
        self.list_of_vertices = csp_problem.graph.list_of_vertices
        self.list_of_variables = csp_problem.graph
        self.number_of_results = 0
        self.number_of_backs = 0

    def backtracking(self, start_vertex):
        if start_vertex is None:
            self.number_of_results += 1
            return
        else:
            vertex = start_vertex
            for supposed_value in vertex.variable.domain:
                vertex.variable.value = supposed_value
                is_valid = self.csp_problem.is_valid_for_entangled_variables(vertex)
                if is_valid:
                    next_vertex = mrv_heuristic(self.list_of_vertices)
                    # next_vertex = self.list_of_vertices[start_vertex.number + 1] if start_vertex.number + 1 < len(
                    #     self.list_of_vertices) else None
                    self.backtracking(next_vertex)
                    self.number_of_backs += 1
            vertex.variable.value = None
