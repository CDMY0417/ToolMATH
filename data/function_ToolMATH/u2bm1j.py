def multiply_mixed_number(integer: int, whole: int, fraction_numerator: int, fraction_denominator: int) -> int:
    return integer * whole + (integer * fraction_numerator) // fraction_denominator
