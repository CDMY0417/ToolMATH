def calculate_combinations(n: int, k: int) -> int:
    if k > n:
        return 0
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))
