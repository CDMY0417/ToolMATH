def mod_exponent_pattern(base: int, mod: int, max_exponent: int):
    pattern = {}
    current = base
    for exponent in range(1, max_exponent + 1):
        remainder = current % mod
        if remainder in pattern.values():
            break
        pattern[exponent] = remainder
        current *= base
    return pattern
