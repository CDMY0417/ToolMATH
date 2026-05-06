def factor_out_gcd_from_terms(a: int, b: int, c: int):
    from math import gcd
    common_gcd = gcd(gcd(a, b), c)
    a_factored = a // common_gcd
    b_factored = b // common_gcd
    c_factored = c // common_gcd
    return common_gcd, a_factored, b_factored, c_factored
