def solve_linear_system_2x2(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    d = a1 * b2 - a2 * b1
    dx = c1 * b2 - c2 * b1
    dy = a1 * c2 - a2 * c1
    if d == 0: return None  # No solution or infinite solutions
    x = dx / d
    y = dy / d
    return x, y
