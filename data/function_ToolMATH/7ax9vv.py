def sum_of_consecutive_integers_b(start: int, n: int) -> int:
    return sum(start + i for i in range(n))
