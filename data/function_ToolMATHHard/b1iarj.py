def solve_rational_functional_equation(x: float):
    """Return f(x) from functional equation."""
    # Solve for A=f(x), B=f(1/x)
    # 3B + 2A/x = x^2
    # 3A + 2Bx = 1/x^2
    # Solve linear system
    A = (x**4 - 3) / (x**2 - 4)
    return A
