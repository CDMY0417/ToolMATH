def merge_prime_factors(factors1: dict[int, int], factors2: dict[int, int]) -> dict[int, int]:
    result = factors1.copy()
    for prime, power in factors2.items():
        if prime in result:
            result[prime] = max(result[prime], power)
        else:
            result[prime] = power
    return result
