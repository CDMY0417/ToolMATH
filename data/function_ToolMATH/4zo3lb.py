def quadratic_roots(a: float, b: float, c: float):
    from math import sqrt
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)
    return (root1, root2)
