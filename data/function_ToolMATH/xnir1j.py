def permutations_of_items(n: int, k: int) -> int:
    product = 1
    for i in range(k):
        product *= n - i
    return product
