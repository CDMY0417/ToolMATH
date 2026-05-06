def combine_like_terms_c(poly1: list[int], poly2: list[int]) -> list[int]:
    max_length = max(len(poly1), len(poly2))
    poly1.extend([0] * (max_length - len(poly1)))
    poly2.extend([0] * (max_length - len(poly2)))
    return [coeff1 + coeff2 for coeff1, coeff2 in zip(poly1, poly2)]
