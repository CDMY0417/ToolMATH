def quadratic_roots_a(a: float, b: float, c: float) -> tuple:
    d = (b ** 2) - (4 * a * c)
    sqrt_val = d ** 0.5
    return ((-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a))
