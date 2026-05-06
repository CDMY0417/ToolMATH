def simplify_fraction_exponent_form(numerator_exponent: int, denominator_exponent: int) -> int:
    if numerator_exponent == denominator_exponent:
        return 1
    return 2**(numerator_exponent - denominator_exponent)
