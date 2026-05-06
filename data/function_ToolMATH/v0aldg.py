def quadratic_has_no_real_roots(a: int, b: int, c: int) -> bool:
    discriminant = b * b - 4 * a * c
    return discriminant < 0
