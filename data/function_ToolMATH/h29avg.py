def solve_quadratic_equation_m(a: float, b: float, c: float):
    from math import sqrt
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2*a)]
    else:
        sqrt_d = sqrt(discriminant)
        return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]
