def combine_fractions_e(num1: float, den1: float, num2: float, den2: float):
    common_denominator = den1 * den2
    numerator = num1 * den2 + num2 * den1
    return numerator, common_denominator
