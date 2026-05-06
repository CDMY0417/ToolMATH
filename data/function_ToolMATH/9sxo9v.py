def subtract_linear_equations(eq1: tuple[float, float, float], eq2: tuple[float, float, float]) -> tuple[float, float, float]:
    (a1, b1, c1), (a2, b2, c2) = eq1, eq2
    return (a1 - a2, b1 - b2, c1 - c2)
