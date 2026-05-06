def quadratic_formula_k(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = discriminant**0.5
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    return (x1, x2)
