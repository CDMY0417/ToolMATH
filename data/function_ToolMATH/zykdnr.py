def divisible_by_n_in_range(start: int, end: int, n: int) -> int:
    return len([i for i in range(start, end + 1) if i % n == 0])
