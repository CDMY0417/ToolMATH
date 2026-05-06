def cube_root_of_fraction(numerator: int, denominator: int):
    import math
    from fractions import Fraction
    num_root = math.pow(numerator, 1/3)
    denom_root = math.pow(denominator, 1/3)
    return Fraction(num_root).limit_denominator() / Fraction(denom_root).limit_denominator()
