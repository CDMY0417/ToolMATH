def add_polynomials(poly1: list[int], poly2: list[int]) -> list[int]:
    max_len = max(len(poly1), len(poly2))
    result = [0] * max_len

    for i in range(len(poly1)):
        result[i + max_len - len(poly1)] += poly1[i]

    for i in range(len(poly2)):
        result[i + max_len - len(poly2)] += poly2[i]

    return result
