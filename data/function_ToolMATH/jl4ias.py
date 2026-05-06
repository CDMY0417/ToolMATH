def subtract_equations_c(eq1: tuple[float, ...], eq2: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(a - b for a, b in zip(eq1, eq2))
