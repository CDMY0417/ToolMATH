def factor_quadratic_w(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    sqrt_d = discriminant**0.5
    if sqrt_d != int(sqrt_d):
        return None
    root1 = (-b + int(sqrt_d)) // (2 * a)
    root2 = (-b - int(sqrt_d)) // (2 * a)
    return (root1, root2) if root1 != root2 else (root1,)
