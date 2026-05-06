def solve_linear_equations_h(a: float, b: float, c: float, d: float):
    # Solve by substitution or elimination
    x = (c * a - d * b) / (a ** 2 - b ** 2)
    y = (c - a * x) / b
    return x, y
