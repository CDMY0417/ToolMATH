def max_three_digit_from_digit_equation(dummy: int = 0):
    """Return maximum NPM."""
    best = None
    for M in range(1, 10):
        prod = 11*M*M
        if 100 <= prod <= 999 and prod % 10 == M:
            if best is None or prod > best:
                best = prod
    return best
