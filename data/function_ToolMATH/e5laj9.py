def count_odd_numbers(start: int, end: int) -> int:
    return len([x for x in range(start, end + 1) if x % 2 != 0])
