def factors_g(n: int) -> list:
    return [i for i in range(1, n + 1) if n % i == 0]
