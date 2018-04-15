def mrv_heuristic(list_of_vertices):
    vertices = get_vertices_without_variable_value(list_of_vertices)
    if len(vertices) == 0:
        return None
    else:
        min_domain_vertex = min(vertices, key=lambda x: len(x.variable.domain))
        return min_domain_vertex


def get_vertices_without_variable_value(list_of_vertices):
    return list(filter(lambda x: x.variable.value is None, list_of_vertices))
