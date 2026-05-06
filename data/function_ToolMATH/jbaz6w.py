def count_inclusive_range(start: int, end: int) -> int:
    if start > end:
        return 0
    return end - start + 1
