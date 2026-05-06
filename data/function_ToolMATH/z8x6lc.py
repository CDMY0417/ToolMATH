def calculate_ratio_g(area1: int, area2: int) -> str:
    from fractions import Fraction
    return str(Fraction(area1, area2))
