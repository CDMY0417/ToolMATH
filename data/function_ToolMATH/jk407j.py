from math import gcd

def simplify_fraction_aa(num: int, denom: int) -> tuple:
    common_divisor = gcd(num, denom)
    return num // common_divisor, denom // common_divisor
