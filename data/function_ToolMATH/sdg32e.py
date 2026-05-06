def solve_linear_system_f(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> tuple:
    det = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)
