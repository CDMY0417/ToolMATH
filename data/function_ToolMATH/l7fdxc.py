def reciprocal_fraction_a(numerator: int, denominator: int):
    from fractions import Fraction
    fraction = Fraction(numerator, denominator)
    reciprocal = 1 / fraction
    return reciprocal.numerator, reciprocal.denominator
