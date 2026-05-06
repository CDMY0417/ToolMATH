def product_of_coefficients_a(coeffs: list[float]) -> float:
    product = 1
    for coeff in coeffs:
        if coeff != 0:
            product *= coeff
    return product
