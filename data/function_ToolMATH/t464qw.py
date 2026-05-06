def last_multiple_within_range(end: int, multiple_of: int) -> int:
    if end % multiple_of == 0:
        return end
    return end - (end % multiple_of)
