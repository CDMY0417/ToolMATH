def arrangement_count(n: int, k: int) -> int:
    result = 1
    for i in range(k):
        result *= n - i
    return result
