def convert_fraction_to_repeating_decimal_a(numerator: int, denominator: int) -> str:
    whole_part = numerator // denominator
    remainder = numerator % denominator
    decimals = ''
    remainders = {}
    position = 0
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = position
        remainder *= 10
        decimals += str(remainder // denominator)
        remainder %= denominator
        position += 1
    if remainder == 0:
        return f"{whole_part}.{decimals}"
    repeat_start = remainders[remainder]
    non_repeating = decimals[:repeat_start]
    repeating = decimals[repeat_start:]
    return f"{whole_part}.{non_repeating}({repeating})"
