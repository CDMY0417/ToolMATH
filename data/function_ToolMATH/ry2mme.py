def count_distinct_pairs(items: list) -> int:
    n = len(items)
    if n < 2:
        return 0
    return n * (n - 1) // 2
