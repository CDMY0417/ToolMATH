def largest_power_under(num: int, base: int) -> int:
    exponent = 0
    while base ** (exponent + 1) <= num:
        exponent += 1
    return exponent
