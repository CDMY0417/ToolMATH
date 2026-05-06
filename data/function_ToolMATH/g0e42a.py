def discriminant_greater_than_zero(a: int, b: int, c: int) -> bool:
    discriminant = b**2 - 4*a*c
    return discriminant > 0
