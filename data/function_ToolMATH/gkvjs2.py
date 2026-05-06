def compute_probability_d(successful: int, total: int) -> (int, int):
    from math import gcd
    common_divisor = gcd(successful, total)
    num = successful // common_divisor
    denom = total // common_divisor
    return num, denom
