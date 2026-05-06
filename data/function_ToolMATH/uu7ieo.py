def least_common_multiple_ac(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    def lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm, numbers)
