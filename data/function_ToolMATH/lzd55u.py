def prime_factor_count_a(exponents: list[int]) -> int:
    count = 1
    for exp in exponents:
        count *= (exp + 1)
    return count
