def sequential_selection_product(n: int, k: int):
    product = 1
    for i in range(k):
        product *= (n - i)
    return product
