def solve_quadratic_v(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_discriminant = int(discriminant**0.5)
    if sqrt_discriminant**2 != discriminant:
        return []
    x1 = (-b + sqrt_discriminant) // (2*a)
    x2 = (-b - sqrt_discriminant) // (2*a)
    return [x for x in (x1, x2) if a*x**2 + b*x + c == 0]
