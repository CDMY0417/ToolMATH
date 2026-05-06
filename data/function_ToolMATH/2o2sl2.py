def count_divisors_a(prime_exponents: list[int]) -> int:
    total_divisors = 1
    for exponent in prime_exponents:
        total_divisors *= (exponent + 1)
    return total_divisors
