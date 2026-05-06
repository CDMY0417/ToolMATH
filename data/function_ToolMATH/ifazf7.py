def total_combinations(counts: list[int]) -> int:
    result = 1
    for count in counts:
        result *= count
    return result
