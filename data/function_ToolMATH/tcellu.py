from math import gcd

def add_fractions_c(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    num1, denom1 = frac1
    num2, denom2 = frac2
    common_denom = denom1 * denom2
    new_num = num1 * denom2 + num2 * denom1
    common_divisor = gcd(new_num, common_denom)
    return (new_num // common_divisor, common_denom // common_divisor)
