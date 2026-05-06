def convert_repeating_decimal(repeating_part: int):
    length_of_repeating = len(str(repeating_part))
    numerator = repeating_part
    denominator = int('9' * length_of_repeating)
    return (numerator, denominator)
