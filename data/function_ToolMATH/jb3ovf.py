def compute_number_of_factors(prime_exponents: list[int]) -> int:
    count = 1
    for exp in prime_exponents:
        count *= (exp + 1)
    return count
