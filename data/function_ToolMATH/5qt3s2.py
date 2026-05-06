def product_of_consecutive_integers_d(start: int, end: int) -> int:
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product
