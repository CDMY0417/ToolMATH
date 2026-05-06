def update_polynomial_terms(current_terms: list[float], quotient_coefficient: float, divisor_terms: list[float]) -> list[float]:
    updated_terms = current_terms[:]  # Copy to avoid in-place changes
    for i in range(len(divisor_terms)):
        if i < len(updated_terms):
            updated_terms[i] -= quotient_coefficient * divisor_terms[i]
        else:
            updated_terms.append(-quotient_coefficient * divisor_terms[i])
    return updated_terms
