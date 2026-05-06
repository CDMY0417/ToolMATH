def solve_quadratic_inequality_a(a: int, b: int, c: int):
    from math import sqrt
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_d = sqrt(discriminant)
    x1 = (-b - sqrt_d) / (2*a)
    x2 = (-b + sqrt_d) / (2*a)
    if a > 0:
        return [(x1, x2)]  # The solution is between the roots
    else:
        return [(-float('inf'), x1), (x2, float('inf'))]  # The solution is outside the roots
