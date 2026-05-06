def least_number_with_prime_factors(primes: list[int], exponent: int) -> int:
    product = 1
    for prime in primes:
        product *= prime ** exponent
    return product
