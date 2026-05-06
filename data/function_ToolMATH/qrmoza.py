def quadratic_minimum(a: float, b: float, c: float):
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    return (vertex_x, vertex_y)
