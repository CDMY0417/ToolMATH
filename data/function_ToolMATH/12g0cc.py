def simplify_fraction_common_term(num: int, denom: int, term: int):
    return (num // term, denom // term) if term != 0 else (num, denom)
