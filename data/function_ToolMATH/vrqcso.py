from fractions import Fraction

def float_to_fraction(value: float) -> Fraction:
    return Fraction(value).limit_denominator()
