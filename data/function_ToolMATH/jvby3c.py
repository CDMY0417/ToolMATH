def combination_a(n: int, k: int) -> int:
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        k = min(k, n - k)
        c = 1
        for i in range(k):
            c = c * (n - i) // (i + 1)
        return c
