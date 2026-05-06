def solve_linear_complex_equation(a: float, b: float, c: float, d: float):
    """Solve a + b*i*z = c + d*i*z for z."""
    denom = b - d
    if denom == 0:
        raise ValueError("No unique solution for z.")
    return -(c - a) / denom * 1j
