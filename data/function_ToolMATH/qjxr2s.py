def convert_fraction_to_repeating_decimal(numerator: int, denominator: int) -> (str, str):
    integer_part = numerator // denominator
    decimal_part = ''
    remainder = numerator % denominator
    remainders = {}
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
    if remainder == 0:
        return f'{integer_part}.{decimal_part}', ''
    repeat_index = remainders[remainder]
    non_repeating = decimal_part[:repeat_index]
    repeating = decimal_part[repeat_index:]
    return f'{integer_part}.{non_repeating}({repeating})', repeating
