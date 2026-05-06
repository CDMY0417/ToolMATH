def first_multiple_in_range(start: int, multiple: int) -> int:
    if start % multiple == 0:
        return start
    return start + (multiple - start % multiple)
