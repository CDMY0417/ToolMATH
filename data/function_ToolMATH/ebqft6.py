def fraction_equal_to_value(numerator: int, denominator: int, target_value: float) -> int:
    x = (target_value * denominator - numerator) / (1 - target_value)
    return int(x)
