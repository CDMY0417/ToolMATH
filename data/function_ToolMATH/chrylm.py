def count_multiples_in_range_f(m: int, start: int, end: int) -> int:
    return (end // m) - ((start - 1) // m)
