def divide_fractions_c(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
