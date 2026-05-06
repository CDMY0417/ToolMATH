def vertex_form_quadratic(a: float, b: float, c: float) -> tuple:
    h = -b / (2 * a)
    k = a * h ** 2 + b * h + c
    return (a, h, k)
