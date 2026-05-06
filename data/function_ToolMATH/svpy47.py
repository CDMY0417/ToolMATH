def repeating_decimal_to_fraction_d(repeating_decimal_str: str):
    # Extract the integer part and the repeating part
    integer_part, repeating_part = repeating_decimal_str.split('.')
    non_repeating, repeating = repeating_part.split('~')
    # Calculate the multiplier based on the length of the repeating part
    multiplier = 10 ** len(non_repeating) * (10 ** len(repeating) - 1)
    # Convert repeating decimal to fraction form
    numerator = int(integer_part + non_repeating + repeating) - int(integer_part + non_repeating)
    return numerator, multiplier
