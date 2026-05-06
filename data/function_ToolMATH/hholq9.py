def gcd_of_list_c(numbers: list[int]):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)
