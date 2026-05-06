def convert_to_fraction(decimal: float):
    from fractions import Fraction
    return Fraction(decimal).limit_denominator()
