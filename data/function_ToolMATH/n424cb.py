from fractions import Fraction
def convert_float_to_fraction(value: float) -> str:
    fraction = Fraction(value).limit_denominator()
    return f'{fraction.numerator}/{fraction.denominator}'
