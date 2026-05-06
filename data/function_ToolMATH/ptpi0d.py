def subtract_fractions_g(a_numerator: int, a_denominator: int, b_numerator: int, b_denominator: int):
    common_denominator = a_denominator * b_denominator
    a_scaled_numerator = a_numerator * b_denominator
    b_scaled_numerator = b_numerator * a_denominator
    result_numerator = a_scaled_numerator - b_scaled_numerator
    return result_numerator, common_denominator
