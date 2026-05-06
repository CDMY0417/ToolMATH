def repeating_decimal_to_fraction(decimal_str: str):
    n = len(decimal_str) - 2
    non_repeating = int(decimal_str[0])
    repeating_part = int(decimal_str[2:])
    numerator = repeating_part - non_repeating
    denominator = 10**n - 1
    return (numerator, denominator)
