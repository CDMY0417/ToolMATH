def factor_quadratic_q(b: int, c: int) -> tuple:
    discriminant = b**2 - 4*c
    if discriminant < 0:
        return ()
    x1 = (-b + discriminant**0.5) / 2
    x2 = (-b - discriminant**0.5) / 2
    return (x1, x2)
