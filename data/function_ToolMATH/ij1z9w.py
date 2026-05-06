def calculate_probability_af(count: int, total: int):
    from fractions import Fraction
    return Fraction(count, total)
