def multiples_of_k_in_interval(k: int, low: int, high: int) -> list:
    return [i for i in range(low + 1, high + 1) if i % k == 0]
