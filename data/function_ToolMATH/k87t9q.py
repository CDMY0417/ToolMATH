from math import gcd

def divide_fractions_b(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    num1, denom1 = frac1
    num2, denom2 = frac2
    new_num = num1 * denom2
    new_denom = denom1 * num2
    common_divisor = gcd(new_num, new_denom)
    return (new_num // common_divisor, new_denom // common_divisor)
