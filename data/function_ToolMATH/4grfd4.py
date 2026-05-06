def product_of_two_elements(s: set):
    from itertools import combinations
    return [a * b for a, b in combinations(s, 2)]
