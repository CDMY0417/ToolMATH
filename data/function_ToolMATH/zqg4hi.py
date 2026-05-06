def polynomial_division_by_linear(poly_coeffs: list[int], c: int):
    n = len(poly_coeffs)
    quotient = [0] * (n - 1)
    remainder = poly_coeffs[0]
    for i in range(1, n):
        quotient[i - 1] = remainder
        remainder = poly_coeffs[i] + remainder * c
    return quotient, remainder
