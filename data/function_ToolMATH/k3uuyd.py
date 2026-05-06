def integer_multiples_in_range(n: int, lo: int, hi: int) -> int:
    start = (lo + n - 1) // n
    end = hi // n
    return max(0, end - start + 1)
