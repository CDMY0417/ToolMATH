def greatest_power_factor(n: int, base: int) -> int:
    exponent = 0
    while n % (base ** (exponent + 1)) == 0:
        exponent += 1
    return exponent
