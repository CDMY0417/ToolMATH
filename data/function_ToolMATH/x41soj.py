def evaluate_quadratic_i(a: int, b: int, c: int):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return None
    root_discriminant = int(discriminant**0.5)
    if root_discriminant * root_discriminant != discriminant:
        return None
    root1 = (-b + root_discriminant) // (2 * a)
    root2 = (-b - root_discriminant) // (2 * a)
    return root1, root2
