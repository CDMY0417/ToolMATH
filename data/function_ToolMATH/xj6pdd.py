from math import gcd

def simplify_fraction_bn(numerator: int, denominator: int):
    factor = gcd(numerator, denominator)
    return (numerator // factor, denominator // factor)
