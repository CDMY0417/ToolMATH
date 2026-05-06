def convert_to_common_fraction(numerator: int, denominator: int) -> str:
    from fractions import Fraction
    return str(Fraction(numerator, denominator).limit_denominator())
