def solve_linear_equations_f(eq1: tuple[float, float, float], eq2: tuple[float, float, float]) -> tuple[float, float]:
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    det = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y
