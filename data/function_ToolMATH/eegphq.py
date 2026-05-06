def log_base_product_of_squares(base: int, numbers: list[int]) -> float:
    import math
    product_of_squares = 1
    for number in numbers:
        product_of_squares *= number ** 2
    result = math.log(product_of_squares) / math.log(base)
    return result
