def add_integer_to_fraction(integer: int, fraction: tuple[int, int]) -> tuple[int, int]:
    numerator, denominator = fraction
    return (integer * denominator + numerator, denominator)
