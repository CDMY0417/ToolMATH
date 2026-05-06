from math import gcd

def greatest_common_divisor_n(a: int, b: int, c: int):
    return gcd(gcd(a, b), c)
