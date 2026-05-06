def multiply_binomials_a(a: int, b: int, c: int, d: int) -> tuple:
    term1 = a * c  # Coefficient of x^2
    term2 = a * d + b * c  # Coefficient of x
    term3 = b * d  # Constant term
    return (term1, term2, term3)
