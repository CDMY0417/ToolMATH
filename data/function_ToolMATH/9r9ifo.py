def multiply_terms_and_sum_coefficients(poly1: list[int], poly2: list[int], power: int) -> int:
    coefficient_sum = 0
    len1, len2 = len(poly1), len(poly2)
    for i in range(len1):
        for j in range(len2):
            if i + j == power:
                coefficient_sum += poly1[i] * poly2[j]
    return coefficient_sum
