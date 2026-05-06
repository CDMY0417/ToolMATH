from fractions import Fraction

def fraction_addition(fractions: list[str]) -> Fraction:
    total = sum(Fraction(f) for f in fractions)
    return total
