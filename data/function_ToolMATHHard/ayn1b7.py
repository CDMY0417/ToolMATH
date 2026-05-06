def solve_linear_equation(A: float, B: float):
    """Solve A*x + B = 0 for x."""
    if A == 0:
        raise ValueError("A must be nonzero.")
    return -B / A
