def combination(n: int, k: int) -> int:
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))
