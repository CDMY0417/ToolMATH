def long_division_decimal_b(numerator: int, denominator: int):
    decimal_sequence = ''
    remainders = {}
    index = 0

    while numerator != 0 and numerator not in remainders:
        remainders[numerator] = index
        numerator *= 10
        quotient_digit = numerator // denominator
        decimal_sequence += str(quotient_digit)
        numerator %= denominator
        index += 1

    if numerator == 0:
        return decimal_sequence, ''
    else:
        repeat_start = remainders[numerator]
        return decimal_sequence[:repeat_start], decimal_sequence[repeat_start:]
