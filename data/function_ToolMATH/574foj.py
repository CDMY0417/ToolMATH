def solve_quadratic_f(A: int, B: int, C: int):
    from math import sqrt
    discriminant = B**2 - 4 * A * C
    if discriminant < 0:
        return None, None
    root1 = (-B + sqrt(discriminant)) / (2 * A)
    root2 = (-B - sqrt(discriminant)) / (2 * A)
    return root1, root2
