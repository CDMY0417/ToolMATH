def factorial_permutation_a(n: int, k: int):
    result = 1
    for i in range(k):
        result *= (n - i)
    return result
