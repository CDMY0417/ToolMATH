def am_gm_inequality_m(values: list):
    from functools import reduce
    from operator import mul
    n = len(values)
    geometric_mean = reduce(mul, values) ** (1/n)
    return n * geometric_mean
