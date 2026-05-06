def convert_base_to_decimal_j(number: str, base: int):
    decimal_value = 0
    power = len(number) - 1
    for digit in number:
        decimal_value += int(digit) * (base ** power)
        power -= 1
    return decimal_value
