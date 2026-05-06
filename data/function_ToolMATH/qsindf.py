def fraction_from_division(numerator: float, denominator: float):
    from fractions import Fraction
    return Fraction(numerator, denominator).limit_denominator()
