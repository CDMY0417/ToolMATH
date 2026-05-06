def quadratic_roots_ab(a: int, b: int, c: int) -> tuple:
    d = b**2 - 4*a*c
    if d < 0:
        return ()  # No real roots
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    return (root1, root2)
