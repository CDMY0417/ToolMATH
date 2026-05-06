def factor_out_gcd_from_terms_a(terms: list[int], gcd: int) -> list[int]:
    return [term // gcd for term in terms]
