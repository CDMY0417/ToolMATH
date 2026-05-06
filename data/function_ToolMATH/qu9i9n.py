def solve_linear_system_e(eq1: tuple, eq2: tuple):
    a, b, c = eq1
    d, e, f = eq2
    det = a * e - b * d
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    return x, y
