def quadratic_factors_a(b: int, c: int) -> tuple:
    discriminant = b**2 - 4*c
    if discriminant < 0:
        return None, None
    else:
        root1 = (b + discriminant**0.5) / 2
        root2 = (b - discriminant**0.5) / 2
        return root1, root2
