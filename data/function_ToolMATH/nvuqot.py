def subtract_fractions_e(numerator1: int, denominator1: int, numerator2: int, denominator2: int) -> (int, int):
    from math import gcd
    common_denom = denominator1 * denominator2
    num1 = numerator1 * denominator2
    num2 = numerator2 * denominator1
    diff_numer = num1 - num2
    common_div = gcd(diff_numer, common_denom)
    return (diff_numer // common_div, common_denom // common_div)
