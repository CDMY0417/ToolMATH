def first_multiple_in_range_a(multiple: int, start: int) -> int:
    if start % multiple == 0:
        return start
    else:
        return (start // multiple + 1) * multiple
