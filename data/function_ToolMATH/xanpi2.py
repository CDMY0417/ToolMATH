def add_fractions_e(num1: int, den1: int, num2: int, den2: int):
    common_denominator = den1 * den2
    new_num1 = num1 * den2
    new_num2 = num2 * den1
    sum_num = new_num1 + new_num2
    return sum_num, common_denominator
