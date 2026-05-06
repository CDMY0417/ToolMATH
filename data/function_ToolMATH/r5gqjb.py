def solve_quadratic_w(a: float, b: float, c: float):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        return [-b / (2 * a)]  # One real root
    else:
        sqrt_discriminant = discriminant ** 0.5
        return [(-b + sqrt_discriminant) / (2 * a), (-b - sqrt_discriminant) / (2 * a)]
