def count_even_numbers_in_interval(start: int, end: int) -> int:
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    return (end - start) // 2 + 1
