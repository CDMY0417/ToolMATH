def convert_decimal_to_simplified_fraction(decimal: float):
    from fractions import Fraction
    return Fraction(decimal).limit_denominator()
