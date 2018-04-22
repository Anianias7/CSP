def mrv_heuristic(list_of_vertices):
    vertices = get_vertices_without_variable_value(list_of_vertices)
    if len(vertices) == 0:
        return None
    else:
        min_domain_vertex = min(vertices, key=lambda x: len(x.variable.domain))
        return min_domain_vertex


def mcv_heuristic(list_of_vertices, adjacency_list):
    vertices = get_vertices_without_variable_value(list_of_vertices)
    if len(vertices) == 0:
        return None
    else:
        min_constraint_variable = min(vertices, key=lambda x: len(adjacency_list[x.number]))
        return min_constraint_variable


def mcv_with_only_unassigned_neighbours_variables(list_of_vertices, adjacency_list):
    vertices = get_vertices_without_variable_value(list_of_vertices)
    neighbours = get_unassigned_variable_value_adjacency_list(vertices, adjacency_list, list_of_vertices)
    if len(vertices) == 0:
        return None
    else:
        min_constraint_variable = min(vertices, key=lambda x: len(neighbours[vertices.index(x)]))
        return min_constraint_variable


def get_vertex_neighbours_without_values(vertex, adjacency_list, list_of_vertices):
    return list(filter(lambda x: list_of_vertices[x].variable.value is None, adjacency_list[vertex.number]))


def get_unassigned_variable_value_adjacency_list(vertices, adjacency_list, list_of_vertices):
    return list(map(lambda x: get_vertex_neighbours_without_values(x, adjacency_list, list_of_vertices),
                    vertices))


def get_vertices_without_variable_value(list_of_vertices):
    return list(filter(lambda x: x.variable.value is None, list_of_vertices))

