def choose_combinations(n: int, k: int):
    if k > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator
