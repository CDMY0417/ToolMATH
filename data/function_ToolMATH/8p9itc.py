def rewrite_fraction(numerator: int, old_denominator: int, new_denominator: int) -> tuple:
    factor = new_denominator // old_denominator
    new_numerator = numerator * factor
    return (new_numerator, new_denominator)
