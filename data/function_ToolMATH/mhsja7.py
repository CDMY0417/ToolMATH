def quadratic_formula_e(a: float, b: float, c: float):
    import cmath
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    return ((-b + discriminant) / (2*a), (-b - discriminant) / (2*a))
