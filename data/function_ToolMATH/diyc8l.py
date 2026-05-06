def gcd_of_list_b(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers) if numbers else None
