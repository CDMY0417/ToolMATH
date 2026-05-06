def quadratic_roots_v(a: float, b: float, c: float) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()
    sqrt_disc = discriminant**0.5
    return ((-b + sqrt_disc) / (2*a), (-b - sqrt_disc) / (2*a))
