def minimum_factor_greater_than(n: int, threshold: int):
    for i in range(threshold + 1, n + 1):
        if n % i == 0:
            return i
    return None
