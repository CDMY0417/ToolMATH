def reconstruct_from_prime_factors(factors: dict[int, int]) -> int:
    result = 1
    for prime, count in factors.items():
        result *= prime ** count
    return result
