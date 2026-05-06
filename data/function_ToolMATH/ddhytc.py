def sum_of_divisors_a(prime_factors: dict[int, int]) -> int:
    sum_divisors = 1
    for prime, exp in prime_factors.items():
        sum_divisors *= (prime**(exp + 1) - 1) // (prime - 1)
    return sum_divisors
