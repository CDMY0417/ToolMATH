def factor_quadratic_x(b: int, c: int):
    delta = b**2 - 4*c
    if delta < 0:
        return None
    sqrt_delta = delta**0.5
    x1 = (-b + sqrt_delta) / 2
    x2 = (-b - sqrt_delta) / 2
    return (x1, x2)
