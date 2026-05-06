def greatest_common_divisor_z(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)
