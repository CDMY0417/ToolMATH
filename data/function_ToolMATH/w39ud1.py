def find_roots_of_quadratic_d(a: int, b: int, c: int) -> list:
    d = b**2 - 4*a*c
    if d < 0:
        return []
    elif d == 0:
        return [-b / (2*a)]
    else:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return [root1, root2]
