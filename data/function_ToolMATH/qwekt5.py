def solve_system_of_two_linear_equations(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) / (b1 * a2 - b2 * a1)
    return x, y
