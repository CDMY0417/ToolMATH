def divide_exponents_b(left_exponents: dict, right_exponents: dict):
    for base in set(left_exponents.keys()).intersection(right_exponents.keys()):
        power_difference = left_exponents[base] - right_exponents[base]
        left_exponents[base] = power_difference
        right_exponents[base] = 0
    return left_exponents, right_exponents
