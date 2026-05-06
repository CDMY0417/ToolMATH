def count_multiples_in_range_q(multiple: int, start: int, end: int) -> int:
    if start % multiple == 0:
        first_multiple = start
    else:
        first_multiple = start + (multiple - start % multiple)
    if end < first_multiple:
        return 0
    return (end - first_multiple) // multiple + 1
