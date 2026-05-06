def evaluate_polynomial_series(x: int, n: int):
    return sum(x**i for i in range(n + 1))
