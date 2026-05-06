def solve_quadratic_b(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        return ()
    sqrt_d = d**0.5
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    return (x1, x2) if x1 != x2 else (x1,)
