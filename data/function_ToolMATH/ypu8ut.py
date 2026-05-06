def solve_linear_system_m(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float):
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None  # No unique solution
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)
