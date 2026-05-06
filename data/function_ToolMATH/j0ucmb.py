def digit_sum_remainder(count_sevens: int, count_threes: int, base: int):
    digit_sum = count_sevens * 7 + count_threes * 3
    return digit_sum % base
