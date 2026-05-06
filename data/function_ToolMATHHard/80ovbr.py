import math

def stars_and_bars_count(n: int, k: int):
    """Return C(n+k-1, k-1) for n>=0, k>=1."""
    if n < 0 or k <= 0:
        raise ValueError("Invalid inputs.")
    N = n + k - 1
    r = k - 1
    # compute combination N choose r
    num = 1
    den = 1
    r = min(r, N - r)
    for i in range(1, r + 1):
        num *= N - r + i
        den *= i
    return num // den
