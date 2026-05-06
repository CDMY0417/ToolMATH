def multiply_j(number: int, times: int) -> int:
    result = 1
    for _ in range(times):
        result *= number
    return result
