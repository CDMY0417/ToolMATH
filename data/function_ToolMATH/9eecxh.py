from fractions import Fraction
def convert_decimal_to_fraction(decimal: float) -> (int, int):
    fraction = Fraction(decimal).limit_denominator()
    return (fraction.numerator, fraction.denominator)
