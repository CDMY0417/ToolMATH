def prime_power_factors(prime: int, power: int, exclude_highest: bool = False):
    factors = [prime**i for i in range(1, power + 1)]
    if exclude_highest:
        factors = factors[:-1]
    return factors
