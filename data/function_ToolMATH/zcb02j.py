def simplify_fraction_bh(numerator: int, denominator: int):
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor
