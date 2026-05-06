def permutation_count(n: int, k: int) -> int:
    product = 1
    for i in range(k):
        product *= (n - i)
    return product
