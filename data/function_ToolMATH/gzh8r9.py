def sum_of_two_elements(s: set) -> list:
    from itertools import combinations
    return [a + b for a, b in combinations(s, 2)]
