from math import gcd

def simplify_fraction_u(numerator: int, denominator: int):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor
