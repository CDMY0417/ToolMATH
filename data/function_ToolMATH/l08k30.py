def combine_linear_equations(a1: tuple, b1: int, a2: tuple, b2: int, mult1: int, mult2: int):
    new_a = tuple(mult1 * x - mult2 * y for x, y in zip(a1, a2))
    new_b = mult1 * b1 - mult2 * b2
    return new_a, new_b
