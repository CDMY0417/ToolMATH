def partial_product(n: int) -> float:
    product = 1.0
    for i in range(2, n + 1):
        product *= (1 - 1/i)
    return product
