def binomial_coefficient_real(x: float, k: int) -> float:
    from math import factorial
    if k == 0:
        return 1.0
    numerator = 1.0
    for i in range(k):
        numerator *= (x - i)
    denominator = factorial(k)
    return numerator / denominator
