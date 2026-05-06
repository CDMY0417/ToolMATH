def largest_perfect_square_below_a(limit: int) -> int:
    n = int(limit**0.5)
    return n * n if n * n < limit else (n - 1) * (n - 1)
