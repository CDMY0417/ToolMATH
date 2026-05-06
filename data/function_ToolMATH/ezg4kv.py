def convert_base_to_decimal_c(number: str, base: int) -> int:
    result = 0
    power = len(number) - 1
    for digit in number:
        result += int(digit) * (base ** power)
        power -= 1
    return result
