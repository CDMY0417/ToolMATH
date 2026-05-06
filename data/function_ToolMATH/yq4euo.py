from math import gcd

def add_fractions_g(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    num1, denom1 = frac1
    num2, denom2 = frac2
    num = num1 * denom2 + num2 * denom1
    denom = denom1 * denom2
    common_divisor = gcd(num, denom)
    return (num // common_divisor, denom // common_divisor)
