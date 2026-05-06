def quadratic_roots_are_integers(a: float, b: int, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sqrt_discriminant = discriminant**0.5
        return sqrt_discriminant.is_integer()
    return False
