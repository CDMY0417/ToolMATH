def positive_factors(n: int):
    factors = []
    n = abs(n)
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
