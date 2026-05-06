def count_integers_excluding(lo: int, hi: int, exclude: int) -> int:
    count = hi - lo + 1
    if lo <= exclude <= hi:
        count -= 1
    return count
