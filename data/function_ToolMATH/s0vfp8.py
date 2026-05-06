def solve_quadratic_equation_z(a: float, b: float, c: float) -> tuple:
    from math import sqrt
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    return (root1, root2)
