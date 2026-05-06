def solve_quadratic_au(a: float, b: float, c: float):
    d = b**2 - 4*a*c
    if d < 0:
        return []  # No real roots
    elif d == 0:
        return [-b / (2*a)]  # One real root
    else:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return [root1, root2]
