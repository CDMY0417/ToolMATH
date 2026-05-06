def factor_out_gcd_a(coefficients: list[int]):
    from math import gcd
    from functools import reduce
    common_divisor = reduce(gcd, coefficients)
    factored = [c // common_divisor for c in coefficients]
    return common_divisor, factored
