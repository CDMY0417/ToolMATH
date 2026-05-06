def polynomial_long_division_a(numerator_coeffs: list[float], denominator_coeffs: list[float]):
    out = []
    remainder = numerator_coeffs[:]
    while len(remainder) >= len(denominator_coeffs):
        lead_coeff_ratio = remainder[0] / denominator_coeffs[0]
        out.append(lead_coeff_ratio)
        subtrahend = [lead_coeff_ratio * d for d in denominator_coeffs] + [0] * (len(remainder) - len(denominator_coeffs))
        remainder = [a - b for a, b in zip(remainder, subtrahend)]
        remainder.pop(0)
    return out, remainder
