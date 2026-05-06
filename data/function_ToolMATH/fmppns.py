def combinations_bm(n: int, k: int) -> int:
    if k > n:
        return 0
    num = 1
    denom = 1
    for i in range(k):
        num *= n - i
        denom *= i + 1
    return num // denom
