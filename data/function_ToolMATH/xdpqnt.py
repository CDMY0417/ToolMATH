from math import gcd

def reduce_fraction_h(numerator: int, denominator: int):
    common_gcd = gcd(numerator, denominator)
    return (numerator // common_gcd, denominator // common_gcd)
