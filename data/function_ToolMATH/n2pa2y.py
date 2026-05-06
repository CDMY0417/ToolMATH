def convert_base_to_decimal_i(number: int, base: int) -> int:
    total = 0
    exponent = 0
    while number > 0:
        digit = number % 10
        total += digit * (base ** exponent)
        number = number // 10
        exponent += 1
    return total
