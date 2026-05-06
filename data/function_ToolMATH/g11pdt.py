def solve_linear_equations_b(eq1: tuple[float, float, float], eq2: tuple[float, float, float]) -> tuple[float, float]:
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    y = (c1*a2 - c2*a1) / (b1*a2 - b2*a1)
    return x, y
