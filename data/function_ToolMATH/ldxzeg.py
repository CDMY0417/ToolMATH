def count_factors_b(n: int, factor: int) -> int:
    count = 0
    i = factor
    while i <= n:
        count += n // i
        i *= factor
    return count
