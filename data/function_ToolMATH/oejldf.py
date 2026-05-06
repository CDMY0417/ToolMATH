def solve_linear_equations_g(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    a = (c1 * b2 - c2 * b1) // (a1 * b2 - a2 * b1)
    b = (c1 - a1 * a) // b1
    return a, b
