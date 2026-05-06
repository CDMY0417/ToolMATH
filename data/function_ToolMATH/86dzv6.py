from math import gcd

def reduce_fraction_l(numerator: int, denominator: int):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor
