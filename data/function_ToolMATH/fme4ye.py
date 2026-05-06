from fractions import Fraction
def positive_difference_of_fractions(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    f1 = Fraction(frac1[0], frac1[1])
    f2 = Fraction(frac2[0], frac2[1])
    result = abs(f1 - f2)
    return result.numerator, result.denominator
