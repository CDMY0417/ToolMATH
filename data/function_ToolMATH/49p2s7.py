def combine_fractions_h(num1: int, den1: int, num2: int, den2: int):
    common_den = den1 * den2
    new_num = num1 * den2 + num2 * den1
    return new_num, common_den
