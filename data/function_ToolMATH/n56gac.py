def is_product_nonzero(values: list[int]) -> bool:
    product = 1
    for value in values:
        product *= value
    return product != 0
