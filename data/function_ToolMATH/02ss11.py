def sum_of_consecutive_integers(start: int, count: int) -> int:
    return count * start + (count * (count - 1) // 2) * 2
