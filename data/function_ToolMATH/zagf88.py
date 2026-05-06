def find_quadratic_vertex(a: float, b: float, c: float):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return (h, k)
