def sum_of_divisors_c(prime_factors: list[int]) -> int:
    from collections import Counter
    factor_counter = Counter(prime_factors)
    total = 1
    for prime, exp in factor_counter.items():
        total *= (prime ** (exp + 1) - 1) // (prime - 1)
    return total
