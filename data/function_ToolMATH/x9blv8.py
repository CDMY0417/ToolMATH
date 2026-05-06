def lcm_from_prime_factors_a(prime_factors: dict[int, int]) -> int:
    lcm = 1
    for prime, power in prime_factors.items():
        lcm *= prime ** power
    return lcm
