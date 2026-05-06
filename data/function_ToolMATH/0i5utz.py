def factor_quadratic(b: int, c: int):
    discriminant = b**2 - 4*c
    if discriminant < 0:
        return None
    root1 = (-b + discriminant**0.5) / 2
    root2 = (-b - discriminant**0.5) / 2
    return (int(root1), int(root2)) if root1.is_integer() and root2.is_integer() else None
