def convert_repeating_decimal_to_fraction_d(decimal: str, repeat_length: int):
    integer_part, fractional_part = decimal.split('.')
    non_repeating = fractional_part[:-repeat_length]
    repeating = fractional_part[-repeat_length:]
    len_non_repeating = len(non_repeating)
    len_repeating = len(repeating)
    non_repeating_number = int(non_repeating) if non_repeating else 0
    repeating_number = int(repeating)
    power_ten_non_repeating = 10 ** len_non_repeating
    power_ten_repeating = 10 ** len_repeating - 1
    numerator = non_repeating_number * power_ten_repeating + repeating_number
    denominator = power_ten_non_repeating * power_ten_repeating
    return (numerator, denominator)
