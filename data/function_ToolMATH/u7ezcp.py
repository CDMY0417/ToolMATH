def am_gm_equality_condition(terms: list[float]) -> bool:
    n = len(terms)
    return all(term == terms[0] for term in terms)
