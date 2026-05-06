def solve_quadratic_equation_ax(a: int, b: int, c: int) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    return (x1, x2)
