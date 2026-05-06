def long_division_polynomials(numerator_coeffs: list[float], denominator_coeffs: list[float]):
    quotient = []
    remainder = numerator_coeffs[:]
    while len(remainder) >= len(denominator_coeffs):
        leading_coeff_ratio = remainder[0] / denominator_coeffs[0]
        quotient.append(leading_coeff_ratio)
        subtract_poly = [leading_coeff_ratio * dc for dc in denominator_coeffs]
        remainder = [rem_c - sub_c for rem_c, sub_c in zip(remainder, subtract_poly)] + remainder[len(subtract_poly):]
        remainder.pop(0)
        while remainder and remainder[0] == 0:
            remainder.pop(0)
    return quotient, remainder
