def factor_quadratic_ap(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d >= 0:
        sqrt_d = d**0.5
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return (x1, x2) if x1 % 1 == 0 and x2 % 1 == 0 else None
    return None
