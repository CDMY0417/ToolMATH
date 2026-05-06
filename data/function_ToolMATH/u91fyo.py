def parabola_vertex_coordinates(a: float, b: float, c: float):
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return h, k
