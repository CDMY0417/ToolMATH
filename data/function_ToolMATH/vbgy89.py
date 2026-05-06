def fraction_from_repeating_decimal_b(repeating_digits: str):
    scale_factor = 10 ** len(repeating_digits)
    numerator = int(repeating_digits)
    denominator = scale_factor - 1
    return numerator, denominator
