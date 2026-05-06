def product_of_first_n_integers(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
