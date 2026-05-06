def find_roots_of_quadratic_b(a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return ()  # No real roots
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        sqrt_discriminant = discriminant ** 0.5
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return (root1, root2)
