def quadratic_common_root(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    num = a1 * b2 - a2 * b1
    den = a1 - a2
    if den == 0:
        return None
    intersect = num / den
    p = a1
    q = b1 - a2 * intersect
    r = c1 - c2 * intersect * intersect
    discriminant = q * q - 4 * p * r
    if discriminant < 0:
        return []
    sqrt_disc = discriminant ** 0.5
    r1 = (-q + sqrt_disc) / (2 * p)
    r2 = (-q - sqrt_disc) / (2 * p)
    return [r1, r2] if r1 != r2 else [r1]
