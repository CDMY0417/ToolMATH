def quadratic_formula_d(a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    root_delta = delta**0.5
    x1 = (-b + root_delta) / (2 * a)
    x2 = (-b - root_delta) / (2 * a)
    return (x1, x2)
