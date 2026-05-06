def greatest_common_factor_h(nums: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, nums)
