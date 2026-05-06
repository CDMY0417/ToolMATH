def perfect_squares_in_interval(lo: int, hi: int) -> int:
    start = int(lo**0.5)
    end = int(hi**0.5)
    if start**2 < lo:
        start += 1
    if end**2 > hi:
        end -= 1
    return end - start + 1
