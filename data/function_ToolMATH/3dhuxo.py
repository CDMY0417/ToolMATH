def convert_repeating_decimal_to_fraction(repeating_part: str) -> tuple[int, int]:
    length = len(repeating_part)
    numerator = int(repeating_part)
    denominator = int('9' * length)
    return numerator, denominator
