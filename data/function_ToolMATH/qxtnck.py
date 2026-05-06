def solve_quadratic_bw(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_discriminant = int(discriminant**0.5)
    if sqrt_discriminant**2 != discriminant:
        return []
    y1 = (-b + sqrt_discriminant) // (2 * a)
    y2 = (-b - sqrt_discriminant) // (2 * a)
    return [y for y in {y1, y2} if a * y**2 + b * y + c == 0]
