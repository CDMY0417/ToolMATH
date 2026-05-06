def solve_quadratic_aw(a: int, b: int, c: int):
    from math import sqrt
    discriminant = b**2 - 4*a*c
    sol1 = (-b + sqrt(discriminant)) / (2*a)
    sol2 = (-b - sqrt(discriminant)) / (2*a)
    return sol1, sol2
