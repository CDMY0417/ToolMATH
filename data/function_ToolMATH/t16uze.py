def binomial_coefficient_ex(n: int, k: int):
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))
