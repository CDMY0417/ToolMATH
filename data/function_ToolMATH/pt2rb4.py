def power_with_positive_zero_base(base: int, exponent: int):
    return 0 if base == 0 and exponent > 0 else base**exponent
