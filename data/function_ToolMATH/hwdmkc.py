def greatest_common_factor_g(integers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, integers)
