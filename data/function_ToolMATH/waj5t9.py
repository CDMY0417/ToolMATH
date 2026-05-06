def integer_interval_ends(start: int, end: int):
    if start >= end:
        return (None, None)
    return (start + 1, end - 1)
