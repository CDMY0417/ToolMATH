def product_of_consecutive_integers_e(start: int, end: int) -> int:
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result
