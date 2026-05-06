def count_multiples_in_range_a(base: int, limit: int) -> int:
    if limit <= base:
        return 0
    return (limit - 1) // base
