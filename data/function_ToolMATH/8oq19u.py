def solve_linear_equation_ah(a: int, b: int, c: int, d: int):
    if a == c:
        return None  # Infinite or no solutions if coefficients of x are the same
    return (d - b) / (a - c)
