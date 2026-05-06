def multiply_fraction_and_integer(integer: int, fraction: tuple) -> int:
    numerator, denominator = fraction
    return integer * numerator // denominator
