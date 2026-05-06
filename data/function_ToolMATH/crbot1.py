def multiply_fractions_i(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    from math import gcd
    num1, denom1 = frac1
    num2, denom2 = frac2
    numerator = num1 * num2
    denominator = denom1 * denom2
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor
