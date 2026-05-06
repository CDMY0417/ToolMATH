def count_divisors(n: int, prime_factors: dict[int, int]) -> int:
    count = 1
    for exponent in prime_factors.values():
        count *= (exponent + 1)
    return count
