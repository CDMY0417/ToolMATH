def solve_quadratic_equation_aa(a: float, b: float, c: float):
    from math import sqrt
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2*a)]
    else:
        return [(-b + sqrt(discriminant)) / (2*a), (-b - sqrt(discriminant)) / (2*a)]
