def factorial_product_b(n: int, k: int):
    product = 1
    for i in range(n, n-k, -1):
        product *= i
    return product
