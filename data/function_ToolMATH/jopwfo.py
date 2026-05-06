def count_multiples_in_range_k(n: int, start: int, end: int) -> int:
    return (end // n) - ((start - 1) // n)
