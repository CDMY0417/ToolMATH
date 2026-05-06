def long_division_decimal_a(a: int, b: int, decimal_places: int):
    quotient = ''
    remainder = a
    for _ in range(decimal_places):
        remainder *= 10
        digit = remainder // b
        remainder %= b
        quotient += str(digit)
        if remainder == 0:
            break
    return quotient
