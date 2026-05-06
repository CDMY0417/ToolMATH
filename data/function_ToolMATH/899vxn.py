def multiplicative_combinations(group_sizes: list[int]) -> int:
    result = 1
    for size in group_sizes:
        result *= size
    return result
