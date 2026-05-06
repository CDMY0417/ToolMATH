def polynomial_modulus(f_coefficients: list[int], g_coefficients: list[int], x: int):
    f_value = sum(coef * (x ** i) for i, coef in enumerate(f_coefficients))
    g_value = sum(coef * (x ** i) for i, coef in enumerate(g_coefficients))
    return f_value % g_value
