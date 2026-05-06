def combinations_count_ah(n: int, k: int):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(k):
        num *= n - i
        denom *= i + 1
    return num // denom
