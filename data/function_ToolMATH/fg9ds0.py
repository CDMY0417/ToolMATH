def convert_to_base_power(number: int, base: int) -> int:
    exp = 0
    while number % base == 0 and number != 1:
        number //= base
        exp += 1
    return exp if number == 1 else None
