def simplify_fraction_bm(part: int, total: int):
    from math import gcd
    greatest_common_divisor = gcd(part, total)
    return part // greatest_common_divisor, total // greatest_common_divisor
