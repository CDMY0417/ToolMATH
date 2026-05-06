def integer_multiples_in_interval(n: int, lo: int, hi: int) -> int:
    start = (lo + n - 1) // n * n
    end = hi // n * n
    if start > hi:
        return 0
    return (end - start) // n + 1
