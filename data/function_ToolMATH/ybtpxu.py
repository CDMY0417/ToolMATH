def simplify_radical_sum(base_coeffs: list[float], base_radical: float) -> float:
    result = sum(base_coeff * base_radical for base_coeff in base_coeffs)
    return result
