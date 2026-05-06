def quadratic_solver(a: float, b: float, c: float):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_disc = math.sqrt(discriminant)
    return [(-b + sqrt_disc) / (2*a), (-b - sqrt_disc) / (2*a)]
