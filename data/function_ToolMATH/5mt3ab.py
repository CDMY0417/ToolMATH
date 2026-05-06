def count_multiples_within_range(start: int, end: int, multiple: int) -> int:
    count = (end // multiple) - (start // multiple)
    if start % multiple == 0:
        count += 1
    return count
