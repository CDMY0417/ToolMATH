from fractions import Fraction

def convert_to_common_fraction_b(value: float):
    return Fraction(value).limit_denominator()
