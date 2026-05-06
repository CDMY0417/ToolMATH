from fractions import Fraction
def add_fractions_k(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)
    result = frac1 + frac2
    return (result.numerator, result.denominator)
