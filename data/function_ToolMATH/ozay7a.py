from math import gcd
from functools import reduce
def greatest_common_factor_p(numbers: list[int]) -> int:
    return reduce(gcd, numbers)
