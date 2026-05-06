def cross_multiply_e(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    left_coefficients = (numerator1, -denominator1)
    right_coefficients = (numerator2, -denominator2)
    return left_coefficients, right_coefficients
