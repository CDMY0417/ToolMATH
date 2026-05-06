from fractions import Fraction

def fraction_to_common(value: float, max_denominator: int) -> str:
    return str(Fraction(value).limit_denominator(max_denominator))
