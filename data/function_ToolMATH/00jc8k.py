def convert_base_to_decimal(number_str: str, base: int) -> int:
    decimal_value = 0
    power = len(number_str) - 1
    for digit in number_str:
        decimal_value += int(digit) * (base ** power)
        power -= 1
    return decimal_value
