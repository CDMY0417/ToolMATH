def factorial_product(n: int, k: int):
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result
