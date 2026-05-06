def add_polynomials_e(poly1: list[int], poly2: list[int]) -> list[int]:
    length = max(len(poly1), len(poly2))
    result = [0] * length
    for i in range(len(poly1)):
        result[i + length - len(poly1)] += poly1[i]
    for i in range(len(poly2)):
        result[i + length - len(poly2)] += poly2[i]
    return result
