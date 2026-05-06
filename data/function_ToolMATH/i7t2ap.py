def polynomial_division_a(f_coeffs: list[float], d_coeffs: list[float]):
    # Initialize quotient and start with highest degree terms
    q_coeffs = [0] * (len(f_coeffs) - len(d_coeffs) + 1)
    remainder = f_coeffs[:]

    for i in range(len(q_coeffs)):
        coefficient = remainder[i] / d_coeffs[0]
        q_coeffs[i] = coefficient
        for j in range(len(d_coeffs)):
            remainder[i + j] -= coefficient * d_coeffs[j]

    # Remove leading zeroes in the remainder
    remainder = [term for term in remainder if term != 0]
    return q_coeffs, remainder if remainder else [0]
