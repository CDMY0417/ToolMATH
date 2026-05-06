def find_common_denominator_d(num1: int, denom1: int, num2: int, denom2: int):
    common_denominator = denom1 * denom2
    new_num1 = num1 * denom2
    new_num2 = num2 * denom1
    sum_numerator = new_num1 + new_num2
    return sum_numerator, common_denominator
