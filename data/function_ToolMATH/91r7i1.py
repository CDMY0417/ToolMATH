def solve_quadratic_bu(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_discriminant = int(discriminant**0.5)
    if sqrt_discriminant**2 != discriminant:
        return []
    root1 = (-b + sqrt_discriminant) // (2*a)
    root2 = (-b - sqrt_discriminant) // (2*a)
    return [root1, root2] if root1 != root2 else [root1]
