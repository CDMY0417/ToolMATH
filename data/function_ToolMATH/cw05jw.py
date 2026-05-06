def simplify_fraction_bq(numerator: int, denominator: int):
    from math import gcd
    greatest_common_divisor = gcd(numerator, denominator)
    return (numerator // greatest_common_divisor, denominator // greatest_common_divisor)
