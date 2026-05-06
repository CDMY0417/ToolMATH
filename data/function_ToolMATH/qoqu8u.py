def find_vertex_form_parameter(vertex: tuple[float, float], point: tuple[float, float], c: float) -> float:
    x_vertex, y_vertex = vertex
    x, y = point
    a = (y - c) / ((x - x_vertex) ** 2)
    return a
