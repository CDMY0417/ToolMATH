def combinations_count_ag(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    num, denom = 1, 1
    for i in range(k):
        num *= n - i
        denom *= i + 1
    return num // denom
