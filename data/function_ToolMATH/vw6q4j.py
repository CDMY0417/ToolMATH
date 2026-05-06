def find_consecutive_integers_around_sqrt(n: int):
    lo = int(n**0.5)
    if lo * lo == n:
        return (lo, lo)
    return (lo, lo + 1)
