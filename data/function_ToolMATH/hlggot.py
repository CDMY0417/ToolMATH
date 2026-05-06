def greatest_common_factor_f(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)
