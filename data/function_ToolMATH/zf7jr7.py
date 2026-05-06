def add_fractions_h(num1: int, denom1: int, num2: int, denom2: int):
    common_denom = denom1 * denom2
    new_num = num1 * denom2 + num2 * denom1
    return new_num, common_denom
