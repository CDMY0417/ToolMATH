def solve_quadratic_roots_a(a: int, b: int, c: int):
    import math
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (root1, root2)
