def smallest_multiple_in_range(multiple: int, start: int) -> int:
    if start % multiple == 0:
        return start
    return (start // multiple + 1) * multiple
