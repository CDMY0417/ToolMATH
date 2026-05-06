def simplify_fraction_sum(numerator: int, denominator: int) -> int:
    from math import gcd
    greatest_common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // greatest_common_divisor
    simplified_denominator = denominator // greatest_common_divisor
    return simplified_numerator + simplified_denominator
