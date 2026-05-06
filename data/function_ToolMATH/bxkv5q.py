def combinations_with_order(n: int, k: int) -> int:
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= n - i
    return result
