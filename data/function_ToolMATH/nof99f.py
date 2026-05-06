def count_factors_from_prime_exponents(exponents: list[int]) -> int:
    count = 1
    for exp in exponents:
        count *= (exp + 1)
    return count
