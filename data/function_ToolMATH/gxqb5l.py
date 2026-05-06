def binomial_coefficient_df(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(1, k + 1):
        num *= n - (k - i)
        denom *= i
    return num // denom
