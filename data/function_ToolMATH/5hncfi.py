def find_vertex_of_parabola_c(a: int, b: int, c: int):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return h, k
