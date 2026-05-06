def solve_quadratic_a(a: float, b: float, c: float):
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return root1, root2
    else:
        return None, None
