def product_of_sequence(start: int, end: int):
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product
