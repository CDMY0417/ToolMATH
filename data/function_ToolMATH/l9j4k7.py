def prime_factor_count(exponents: list[int]) -> int:
    count = 1
    for exponent in exponents:
        count *= (exponent + 1)
    return count
