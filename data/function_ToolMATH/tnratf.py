def count_multiples_in_range_t(k: int, start: int, end: int) -> int:
    return (end // k) - ((start - 1) // k)
