def first_multiple_within_range(start: int, multiple_of: int) -> int:
    if start % multiple_of == 0:
        return start
    return start + (multiple_of - start % multiple_of)
