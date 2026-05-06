def prime_power_to_number(factors: dict[int, int]) -> int:
    result = 1
    for prime, exponent in factors.items():
        result *= prime ** exponent
    return result
