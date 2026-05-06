def solve_linear_system_c(eq1: tuple[int, int, int], eq2: tuple[int, int, int]) -> tuple[int, int]:
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    # Eliminate b
    factor = b2 / b1
    a2 -= a1 * factor
    c2 -= c1 * factor
    # Solve for x
    x = c2 / a2
    # Substitute back to find y
    y = (c1 - a1 * x) / b1
    return int(x), int(y)
