def vertex_of_parabola_e(a: float, b: float, c: float):
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    return (x_vertex, y_vertex)
