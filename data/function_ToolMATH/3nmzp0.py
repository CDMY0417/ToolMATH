def evaluate_power_with_sign(base: int, exponent: int):
    if exponent % 2 == 0:
        return abs(base) ** exponent
    else:
        return -abs(base) ** exponent
