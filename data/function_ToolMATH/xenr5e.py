def count_odd_numbers_in_range(start: int, end: int) -> int:
    if start % 2 == 0:
        start += 1
    if end % 2 == 0:
        end -= 1
    if start > end:
        return 0
    return ((end - start) // 2) + 1
