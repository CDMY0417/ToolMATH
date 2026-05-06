def smallest_integer_geq(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)
