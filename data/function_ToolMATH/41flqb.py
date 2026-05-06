def fraction_of_total(part: int, total: int) -> str:
    from fractions import Fraction
    return str(Fraction(part, total))
