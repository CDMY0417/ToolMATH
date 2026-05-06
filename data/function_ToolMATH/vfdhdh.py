def sum_of_product_pairs(elements: list[float]) -> float:
    n = len(elements)
    return sum(elements[i] * elements[j] for i in range(n) for j in range(i+1, n))
