def convert_to_common_denominator_b(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * (common_denominator // denominator1)
    new_numerator2 = numerator2 * (common_denominator // denominator2)
    return new_numerator1, common_denominator, new_numerator2, common_denominator
