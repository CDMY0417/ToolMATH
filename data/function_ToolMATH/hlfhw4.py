def multiply_prime_factors(factors: dict[int, int]) -> int:
    product = 1
    for prime, exp in factors.items():
        product *= prime ** exp
    return product
