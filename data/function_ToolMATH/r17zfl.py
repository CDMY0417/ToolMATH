def calculate_product_sequence(start: int, end: int):
    product = 1
    for k in range(start, end + 1):
        product *= (k - 1) / k
    return product
