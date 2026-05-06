def add_fractions_f(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * (common_denominator // denominator1)
    new_numerator2 = numerator2 * (common_denominator // denominator2)
    result_numerator = new_numerator1 + new_numerator2
    return result_numerator, common_denominator
