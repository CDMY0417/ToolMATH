def convert_base_to_decimal_a(number_str: str, base: int) -> int:
    decimal_value = 0
    length = len(number_str)
    for i, digit in enumerate(number_str):
        decimal_value += int(digit) * (base ** (length - i - 1))
    return decimal_value
