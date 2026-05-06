def merge_factorizations(factorization1: dict[int, int], factorization2: dict[int, int]) -> dict[int, int]:
    merged = factorization1.copy()
    for prime, power in factorization2.items():
        if prime in merged:
            merged[prime] = max(merged[prime], power)
        else:
            merged[prime] = power
    return merged
