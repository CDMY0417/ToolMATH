def combine_like_terms_e(expression1: dict, expression2: dict) -> dict:
    combined = expression1.copy()
    for term, coefficient in expression2.items():
        combined[term] = combined.get(term, 0) + coefficient
    return combined
