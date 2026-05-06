def convert_base_to_decimal_l(digits: list[int], base: int) -> int:
    decimal_value = 0
    power = len(digits) - 1
    for digit in digits:
        decimal_value += digit * (base ** power)
        power -= 1
    return decimal_value
