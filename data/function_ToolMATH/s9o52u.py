def distribute_terms_b(coefficient: int, expression: dict[str, int]) -> dict[str, int]:
    return {term: coefficient * value for term, value in expression.items()}
