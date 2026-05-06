def prime_factorization_divisors(exponents: list[int]) -> int:
    divisors_count = 1
    for exponent in exponents:
        divisors_count *= (exponent + 1)
    return divisors_count
