def solve_linear_equations_e(eq1: tuple[float, float, float], eq2: tuple[float, float, float]) -> tuple[float, float]:
    (a1, b1, c1), (a2, b2, c2) = eq1, eq2
    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
    y = (c1 - a1 * x) / b1 if b1 != 0 else (c2 - a2 * x) / b2
    return (x, y)
