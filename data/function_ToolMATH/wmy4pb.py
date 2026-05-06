def find_periodic_term(index: int, terms: list[int]) -> int:
    period = len(terms)
    return terms[index % period]
