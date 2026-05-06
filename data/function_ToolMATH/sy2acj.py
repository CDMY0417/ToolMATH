from math import factorial
def binomial_coefficient_bx(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))
