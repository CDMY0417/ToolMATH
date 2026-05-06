def convert_repeating_decimal_to_fraction_a(integer_part: int, repeating_part: str) -> tuple:
    num_repeating_digits = len(repeating_part)
    non_repeating_value = int(repeating_part)
    denominator = 10**num_repeating_digits - 1
    numerator = integer_part * denominator + non_repeating_value
    return numerator, denominator
