def horizontal_asymptote_of_rational_function_b(numerator_coeffs: list[float], denominator_coeffs: list[float]) -> float:
    if len(numerator_coeffs) < len(denominator_coeffs):
        return 0.0
    elif len(numerator_coeffs) > len(denominator_coeffs):
        return float('inf')
    else:
        return numerator_coeffs[0] / denominator_coeffs[0]
