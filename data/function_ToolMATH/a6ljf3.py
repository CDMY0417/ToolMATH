def factor_out(terms: list[int]):
    from math import gcd
    from functools import reduce
    def list_gcd(lst):
        return reduce(gcd, lst)
    common_factor = list_gcd(terms)
    return common_factor, [term // common_factor for term in terms]
