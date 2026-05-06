def factor_and_simplify_fraction(numerator: int, denominator: int):
    from math import gcd
    common_factor = gcd(numerator, denominator)
    numerator //= common_factor
    denominator //= common_factor
    return (numerator, denominator)
