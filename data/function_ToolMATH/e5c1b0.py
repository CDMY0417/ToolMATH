def merge_factors(factors1: dict[int, int], factors2: dict[int, int]) -> dict[int, int]:
    combined = factors1.copy()
    for prime, power in factors2.items():
        if prime in combined:
            combined[prime] += power
        else:
            combined[prime] = power
    return combined
