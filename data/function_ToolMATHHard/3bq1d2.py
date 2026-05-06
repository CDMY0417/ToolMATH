from fractions import Fraction

def sum_repeating_decimals():
    # 0.4̅8 = 44/90 = 22/45, 0.̅37 = 37/99
    return Fraction(22,45) + Fraction(37,99)
