def apply_exponent_rule(base: tuple, exponent: int):
    a, b = base
    if exponent < 0:
        return (b, a), -exponent
    return base, exponent
