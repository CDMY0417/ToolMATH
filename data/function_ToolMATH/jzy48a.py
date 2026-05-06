def find_x_given_y_plus_inverse(y: float):
    discriminant = y**2 - 4
    if discriminant < 0:
        return []
    sqrt_discriminant = discriminant**0.5
    x1 = (y + sqrt_discriminant) / 2
    x2 = (y - sqrt_discriminant) / 2
    return [x1, x2] if x1 != x2 else [x1]
