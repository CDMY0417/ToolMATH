def long_division_decimal(numerator: int, denominator: int) -> (str, str):
    decimal_part = ''
    seen_remainders = {}
    remainder = numerator % denominator
    while remainder != 0 and remainder not in seen_remainders:
        seen_remainders[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
    if remainder == 0:
        return decimal_part, ''
    else:
        repeat_start = seen_remainders[remainder]
        return decimal_part[:repeat_start], decimal_part[repeat_start:]
