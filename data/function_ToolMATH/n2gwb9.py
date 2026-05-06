def solve_quadratic_equation_t(a: float, b: float, c: float) -> list:
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sqrt_d = discriminant**0.5
        return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]
    return []
