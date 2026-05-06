def ones_digit_of_power_of_2(exponent: int) -> int:
    ones_digits = [6, 2, 4, 8]
    return ones_digits[exponent % 4]
