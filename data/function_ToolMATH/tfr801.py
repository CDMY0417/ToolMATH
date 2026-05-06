def solve_linear_equations_2x2(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    determinant = a1 * b2 - b1 * a2
    x = (c1 * b2 - b1 * c2) / determinant
    y = (a1 * c2 - c1 * a2) / determinant
    return (x, y)
