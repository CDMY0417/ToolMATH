def multiples_in_interval(k: int, lo: int, hi: int) -> int:
    first_multiple = (lo + k - 1) // k
    last_multiple = hi // k
    return last_multiple - first_multiple + 1
