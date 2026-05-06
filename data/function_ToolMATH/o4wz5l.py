def multiply_fractions_o(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    from math import gcd
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
