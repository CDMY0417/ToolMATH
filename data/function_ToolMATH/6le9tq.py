def log_base_10_of_factorial(n: int) -> float:
    from math import log10
    return sum(log10(i) for i in range(2, n + 1))
