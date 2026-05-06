def multiples_in_interval_a(multiple_of: int, lo: int, hi: int) -> list:
    start = (lo + multiple_of - 1) // multiple_of * multiple_of
    return list(range(start, hi + 1, multiple_of))
