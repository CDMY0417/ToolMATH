from fractions import Fraction


def multiply_fractions_r(fractions: list[Fraction]) -> Fraction:
    product = Fraction(1, 1)
    for frac in fractions:
        product *= frac
    return product
