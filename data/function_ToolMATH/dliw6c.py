def convert_to_terminating_decimal(numerator: int, denominator: int) -> float:
    from fractions import Fraction
    fraction = Fraction(numerator, denominator)
    return float(fraction)
