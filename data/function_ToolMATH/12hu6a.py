def count_arrangements_without_repetition(n: int, k: int) -> int:
    from math import factorial
    return factorial(n) // factorial(n - k)
