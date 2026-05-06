def sum_fractions_b(fraction1: tuple[int, int], fraction2: tuple[int, int]):
    from fractions import Fraction
    f1 = Fraction(fraction1[0], fraction1[1])
    f2 = Fraction(fraction2[0], fraction2[1])
    return f1 + f2
