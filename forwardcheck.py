from heuristics import mrv_heuristic


class ForwardCheck:

    def __init__(self, csp_problem):
        self.latin_square = csp_problem
        self.list_of_vertices = csp_problem.graph.list_of_vertices
        self.adjacency_list = csp_problem.graph.adjacency_list
        self.number_of_results = 0
        self.number_of_backs = 0

    def forwardchecking(self, start_vertex):
        if start_vertex is None:
            self.number_of_results += 1
            return
        else:
            vertex = start_vertex
            for supposed_value in vertex.variable.domain:
                vertex.variable.value = supposed_value
                is_valid = self.latin_square.is_valid_for_entangled_variables(vertex)

                saved_domains = self.__save_domain(vertex)
                self.__reduce_domain(vertex)
                next_vertex = mrv_heuristic(self.list_of_vertices)
                # next_vertex = self.list_of_vertices[start_vertex.number + 1] if start_vertex.number + 1 < len(
                #     self.list_of_vertices) else None
                self.forwardchecking(next_vertex)
                self.__restore_domain(vertex, saved_domains)
                self.number_of_backs += 1
        vertex.variable.value = None

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
