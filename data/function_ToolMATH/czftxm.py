def add_equations(eq1: tuple[float, ...], eq2: tuple[float, ...]) -> tuple[float, ...]:
    result_eq = tuple(a + b for a, b in zip(eq1, eq2))
    return result_eq
