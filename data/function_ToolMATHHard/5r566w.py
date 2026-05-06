def solve_two_linear_equations(A1: float, B1: float, C1: float, A2: float, B2: float, C2: float):
    """Solve a 2x2 linear system."""
    det = A1 * B2 - A2 * B1
    if det == 0:
        raise ValueError("System has no unique solution.")
    u = (C1 * B2 - C2 * B1) / det
    v = (A1 * C2 - A2 * C1) / det
    return (u, v)
