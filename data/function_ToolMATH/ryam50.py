def count_adjacent_multiples_in_range(start: int, end: int, divisor: int) -> int:
    return len([i for i in range(start, end + 1) if (i + 1) % divisor == 0])
