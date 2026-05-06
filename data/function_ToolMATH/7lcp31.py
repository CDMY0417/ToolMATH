def sum_of_integers_in_interval(start: int, end: int) -> int:
    n = end - start + 1
    return (n * (start + end)) // 2
