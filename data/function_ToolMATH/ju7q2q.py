def sum_of_consecutive_integers_f(start: int, end: int) -> int:
    n = end - start + 1
    return n * (start + end) // 2
