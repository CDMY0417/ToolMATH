def simplify_polynomial_product(coeffs: list[float], powers: list[int]):
    total_coeff = 1
    total_power = 0
    for i in range(len(coeffs)):
        total_coeff *= coeffs[i]
        total_power += powers[i]
    return total_coeff, total_power
