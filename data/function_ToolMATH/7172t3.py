def convert_fraction(numerator: int, denominator: int, new_denominator: int) -> tuple:
    factor = new_denominator // denominator
    new_numerator = numerator * factor
    return new_numerator, new_denominator
