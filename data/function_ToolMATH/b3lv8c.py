from fractions import Fraction
def simplify_fraction_ba(numerator: int, denominator: int):
    fraction = Fraction(numerator, denominator)
    return fraction.numerator, fraction.denominator
