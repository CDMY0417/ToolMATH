def combinations_count_y(n: int, k: int) -> int:
    if k > n:
        return 0
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c
