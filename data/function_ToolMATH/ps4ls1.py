def subtract_fractions_f(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    from fractions import Fraction
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)
    result = fraction1 - fraction2
    return result.numerator, result.denominator
