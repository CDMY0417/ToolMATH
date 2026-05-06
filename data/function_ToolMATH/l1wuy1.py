def lowest_common_multiple_a(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    def lcm(x, y):
        return x * y // gcd(x, y)
    return reduce(lcm, numbers)
