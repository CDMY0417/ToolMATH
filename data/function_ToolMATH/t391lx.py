def collect_like_terms_a(terms: list):
    from sympy import simplify
    return simplify(sum(terms))
