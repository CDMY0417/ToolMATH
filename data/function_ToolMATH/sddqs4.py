def log_base_fraction(base_numerator: int, base_denominator: int, num: int) -> float:
    base = base_numerator / base_denominator
    exponent = 0
    while base ** exponent != num:
        exponent -= 1
    return exponent
