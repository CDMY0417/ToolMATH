def convert_base_to_decimal_f(number: int, base: int) -> int:
    decimal_value = 0
    power = 0
    while number > 0:
        last_digit = number % 10
        decimal_value += last_digit * (base ** power)
        power += 1
        number //= 10
    return decimal_value
