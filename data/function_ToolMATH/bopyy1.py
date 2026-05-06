def closest_perfect_square(n: int) -> int:
    lo = int(n**0.5)
    hi = lo + 1
    if abs(lo**2 - n) <= abs(hi**2 - n):
        return lo**2
    else:
        return hi**2
