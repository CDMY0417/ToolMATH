def sum_neg_one_powers(start: int, end: int) -> int:
    return sum((-1) ** n for n in range(start, end + 1))
