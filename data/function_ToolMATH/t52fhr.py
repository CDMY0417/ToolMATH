def sum_of_consecutive_integers_j(start: int, end: int) -> int:
    return (end * (end + 1) // 2) - (start * (start - 1) // 2)
