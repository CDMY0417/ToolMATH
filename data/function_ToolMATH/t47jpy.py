def greatest_common_factor_o(numbers: list[int]) -> int:
    from functools import reduce
    from math import gcd
    return reduce(gcd, numbers)
