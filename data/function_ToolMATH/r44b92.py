def adjusted_triples_count(initial_count: int, specific_cases: int, unordered_pairs: bool) -> int:
    count = initial_count - specific_cases
    if unordered_pairs:
        count //= 2
    return specific_cases + count
