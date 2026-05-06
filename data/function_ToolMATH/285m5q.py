def factor_quadratic_c(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    p = (-b + discriminant**0.5) / (2*a)
    q = (-b - discriminant**0.5) / (2*a)
    return (p, q)
