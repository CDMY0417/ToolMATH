def polynomial_long_division(numerator_coeffs: list[float], denominator_coeffs: list[float]):
    quotient = []
    remainder = numerator_coeffs[:]
    while len(remainder) >= len(denominator_coeffs):
        coeff = remainder[0] / denominator_coeffs[0]
        quotient.append(coeff)
        for i in range(len(denominator_coeffs)):
            remainder[i] -= coeff * denominator_coeffs[i]
        remainder = remainder[1:]
    return quotient, remainder
