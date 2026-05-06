def multiply_fractions_ab(num1: int, den1: int, num2: int, den2: int):
    from math import gcd
    numerator = num1 * num2
    denominator = den1 * den2
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
