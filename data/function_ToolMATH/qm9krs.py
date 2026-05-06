def count_odd_numbers_in_interval(start: int, end: int) -> int:
    return (end - start) // 2 + 1 if start % 2 == 1 else (end - start + 1) // 2
