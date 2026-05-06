def gcd_multiple(nums: list[int]) -> int:
    from functools import reduce
    from math import gcd
    return reduce(gcd, nums)
