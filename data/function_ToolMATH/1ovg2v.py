def factor_out_gcd(terms: list[int]) -> list[int]:
    from math import gcd
    from functools import reduce

    def compute_gcd(numbers):
        return reduce(gcd, numbers)

    term_gcd = compute_gcd(terms)
    return [term_gcd] + [term // term_gcd for term in terms]
