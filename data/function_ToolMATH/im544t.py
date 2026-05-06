def add_polynomials_d(poly1: list[int], poly2: list[int]) -> list[int]:
    return [a + b for a, b in zip(poly1, poly2)] + poly1[len(poly2):] + poly2[len(poly1):]
