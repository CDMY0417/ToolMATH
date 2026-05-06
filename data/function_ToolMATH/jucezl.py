def quadratic_solutions(constant: int):
    import math
    discriminant = 1 + 4 * constant
    if discriminant < 0:
        return []  # No real solutions
    sqrt_disc = math.sqrt(discriminant)
    y1 = (-1 + sqrt_disc) / 2
    y2 = (-1 - sqrt_disc) / 2
    return [y1, y2]
