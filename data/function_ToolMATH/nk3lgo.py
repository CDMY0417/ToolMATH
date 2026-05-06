def combinations_v(n: int, k: int):
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))
