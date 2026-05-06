def combinations_ao(n: int, k: int) -> int:
    if k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n - (k - i)
        denominator *= i
    return numerator // denominator
