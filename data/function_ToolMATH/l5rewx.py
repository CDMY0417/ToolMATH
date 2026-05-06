def factor_quadratic_r(a: int, b: int, c: int) -> int:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 0  # two complex roots
    elif discriminant == 0:
        return 1  # one real root
    else:
        return 2  # two distinct real roots
