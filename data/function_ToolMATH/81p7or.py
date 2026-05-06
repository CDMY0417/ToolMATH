def octal_to_decimal(octal_number: int) -> int:
    decimal_value = 0
    power = 0
    while octal_number > 0:
        decimal_value += (octal_number % 10) * (8 ** power)
        octal_number //= 10
        power += 1
    return decimal_value
