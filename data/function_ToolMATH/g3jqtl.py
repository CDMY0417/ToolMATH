def decimal_expansion(numerator: int, denominator: int):
    seen_remainders = {}
    decimal_part = ''
    remainder = numerator % denominator
    while remainder != 0:
        if remainder in seen_remainders:
            start = seen_remainders[remainder]
            return decimal_part[:start], decimal_part[start:]
        seen_remainders[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
    return decimal_part, ''
