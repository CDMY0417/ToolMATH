def apply_exponent_to_prime_factors(prime_factors: dict, exponent: int):
    return {prime: base_exp * exponent for prime, base_exp in prime_factors.items()}
