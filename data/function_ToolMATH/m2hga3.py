def solve_linear_system_of_two_equations(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))
    return x, y
