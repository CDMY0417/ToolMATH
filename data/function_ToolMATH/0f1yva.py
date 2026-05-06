def solve_polynomial(coefficients: list[float]):
    if len(coefficients) == 3:  # quadratic case
        a, b, c = coefficients
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            return [(-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a)]
    return []  # Placeholder for non-quadratic cases
