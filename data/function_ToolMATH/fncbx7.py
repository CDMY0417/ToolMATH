def positive_factors_b(n: int):
    return [i for i in range(1, n) if n % i == 0]
