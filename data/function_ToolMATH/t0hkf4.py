def subtract_fractions_j(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1
    result_numerator = new_numerator1 - new_numerator2
    result_denominator = common_denominator
    return result_numerator, result_denominator
