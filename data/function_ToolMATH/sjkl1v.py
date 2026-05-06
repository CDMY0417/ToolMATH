def combine_like_terms_b(poly1: list[int], poly2: list[int]) -> list[int]:
    max_len = max(len(poly1), len(poly2))
    poly1 = poly1 + [0] * (max_len - len(poly1))
    poly2 = poly2 + [0] * (max_len - len(poly2))
    return [a + b for a, b in zip(poly1, poly2)]
