from fractions import Fraction

def decimal_to_fraction(decimal: float):
    return Fraction(decimal).limit_denominator()
