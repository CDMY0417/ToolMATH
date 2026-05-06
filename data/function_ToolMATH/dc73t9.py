from fractions import Fraction

def add_fractions_i(frac1: tuple[int, int], frac2: tuple[int, int]) -> Fraction:
    f1 = Fraction(frac1[0], frac1[1])
    f2 = Fraction(frac2[0], frac2[1])
    return f1 + f2
