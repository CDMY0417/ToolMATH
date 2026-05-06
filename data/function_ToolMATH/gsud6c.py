def quadratic_formula_j(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return (x1, x2)
    else:
        return None
