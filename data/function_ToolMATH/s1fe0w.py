def fraction_difference_d(frac1: tuple[int, int], frac2: tuple[int, int]):
    from fractions import Fraction
    f1 = Fraction(frac1[0], frac1[1])
    f2 = Fraction(frac2[0], frac2[1])
    return f1 - f2
