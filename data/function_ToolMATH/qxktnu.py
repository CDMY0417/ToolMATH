def combination_count_b(n: int, k: int) -> int:
    if k > n:
        return 0
    num = 1
    denom = 1
    for i in range(1, k + 1):
        num *= (n - i + 1)
        denom *= i
    return num // denom
