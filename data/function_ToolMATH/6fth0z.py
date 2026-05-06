def permutations_of_k_from_n(n: int, k: int) -> int:
    result = 1
    for i in range(k):
        result *= (n - i)
    return result
