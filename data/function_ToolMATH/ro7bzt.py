def product_of_integers_c(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
