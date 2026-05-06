def find_common_denominator_b(frac1: tuple[int, int], frac2: tuple[int, int]) -> int:
    from math import gcd
    num1, denom1 = frac1
    num2, denom2 = frac2
    lcm_denominator = denom1 * denom2 // gcd(denom1, denom2)
    return lcm_denominator
