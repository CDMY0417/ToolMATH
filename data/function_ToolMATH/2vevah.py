def combinations_ax(n: int, k: int) -> int:
    if k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
