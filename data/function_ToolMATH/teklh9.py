def distribute_term_a(term: int, expressions: list[int]) -> list[int]:
    return [term * expr for expr in expressions]
