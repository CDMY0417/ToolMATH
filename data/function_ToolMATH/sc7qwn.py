def product_of_square_roots(expressions: list[float]) -> float:
    product = 1
    for expr in expressions:
        product *= expr**0.5
    return product
