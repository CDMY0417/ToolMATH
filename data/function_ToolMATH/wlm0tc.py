def polynomial_division_step(dividend_coefficient: int, divisor_leading_coefficient: int, degree_difference: int):
    return dividend_coefficient // divisor_leading_coefficient if degree_difference >= 0 else 0
