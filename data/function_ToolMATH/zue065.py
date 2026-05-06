def solve_quadratic_bi(a: float, b: float, c: float) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + discriminant**(0.5)) / (2*a)
        root2 = (-b - discriminant**(0.5)) / (2*a)
        return root1, root2
    return None, None
