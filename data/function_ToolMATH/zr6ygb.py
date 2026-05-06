def binomial_coefficient_cn(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n
        denominator *= i
        n -= 1
    return numerator // denominator
