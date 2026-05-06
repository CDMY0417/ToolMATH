def sum_odd_integers(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1) if i % 2 != 0)
