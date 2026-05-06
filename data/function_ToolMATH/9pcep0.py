def subtract_fractions_l(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    import math
    num1, den1 = frac1
    num2, den2 = frac2
    common_den = den1 * den2
    num1 *= den2
    num2 *= den1
    difference = num1 - num2
    gcd = math.gcd(difference, common_den)
    return (difference // gcd, common_den // gcd)
