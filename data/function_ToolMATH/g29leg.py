def binomial_coefficient_al(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n - (i - 1)
        denominator *= i
    return numerator // denominator
