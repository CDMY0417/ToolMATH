def calculate_root_from_discriminant(a: float, b: float, discriminant: float) -> tuple:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return (root1, root2)
