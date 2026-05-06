from fractions import Fraction
def multiply_fractions_f(frac1: tuple[int, int], frac2: tuple[int, int]):
    f1 = Fraction(frac1[0], frac1[1])
    f2 = Fraction(frac2[0], frac2[1])
    result = f1 * f2
    return result.numerator, result.denominator
