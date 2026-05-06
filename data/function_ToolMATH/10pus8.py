def sum_of_consecutive_integers_p(start: int, end: int) -> int:
    return (end - start + 1) * (start + end) // 2
