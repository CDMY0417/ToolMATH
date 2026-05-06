def multiples_inclusive_count(m: int, start: int, end: int) -> int:
    first_multiple = ((start + m - 1) // m) * m
    last_multiple = (end // m) * m
    if first_multiple > end:
        return 0
    return (last_multiple - first_multiple) // m + 1
