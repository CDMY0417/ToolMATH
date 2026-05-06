def find_multiple_in_range(m: int, lo: float, hi: float):
    lo_int = int(lo) + 1
    hi_int = int(hi)
    for n in range(lo_int, hi_int):
        if n % m == 0:
            return n
    return None
