def discriminant_nonnegative_condition(a: float, b: float, c: float) -> bool:
    discriminant = b ** 2 - 4 * a * c
    return discriminant >= 0
