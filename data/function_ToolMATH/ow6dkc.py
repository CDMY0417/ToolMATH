def am_gm_inequality_k(terms: list[float]) -> bool:
    n = len(terms)
    product = 1
    for term in terms:
        product *= term
    return sum(terms) >= n * (product ** (1/n))
