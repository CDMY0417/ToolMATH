from math import gcd
from functools import reduce

def factor_out_gcd_b(coefficients: list[int]):
    coefficients_gcd = reduce(gcd, coefficients)
    return [c // coefficients_gcd for c in coefficients], coefficients_gcd
