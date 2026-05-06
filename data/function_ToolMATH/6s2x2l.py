def quadratic_roots_s(a: float, b: float, c: float):
    d = b**2 - 4*a*c
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    return root1, root2
