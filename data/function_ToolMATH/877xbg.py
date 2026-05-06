def arrangements_without_repetition(n: int, k: int):
    result = 1
    for i in range(k):
        result *= n - i
    return result
