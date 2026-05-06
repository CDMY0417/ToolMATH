def subtract_invalid_combinations(total: int, combinations_removed: list[int]) -> int:
    invalid_total = sum(combinations_removed)
    return total - invalid_total
