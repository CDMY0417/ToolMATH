def least_common_multiple_aa(a: int, b: int, c: int) -> int:
    from math import gcd
    lcm_ab = a * b // gcd(a, b)
    lcm_abc = lcm_ab * c // gcd(lcm_ab, c)
    return lcm_abc
