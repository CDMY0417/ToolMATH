def pair_products_b(numbers: list[int]) -> list[int]:
    from itertools import combinations
    return [a * b for a, b in combinations(numbers, 2)]
