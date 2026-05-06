def base_into_sum_remainder(x1: int, x2: int, base: int):
    sum_value = x1 + x2
    quotient = sum_value // base
    remainder = sum_value % base
    return quotient, remainder
