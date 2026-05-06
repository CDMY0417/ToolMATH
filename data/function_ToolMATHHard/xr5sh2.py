def solve_rational_functional_equation_value(x: float):
    """Return f(x) for 3 f(1/x) + 2 f(x)/x = x^2."""
    if x == 0:
        raise ValueError("x must be nonzero.")
    return (3 - 2*(x**5)) / (5 * x**2)
