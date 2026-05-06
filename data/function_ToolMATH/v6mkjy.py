def quadratic_formula_r(a: float, b: float, c: float) -> tuple:
    import math
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (root1, root2)
