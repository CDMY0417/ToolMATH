def prime_factorize_exponentiation(base_factors: dict, power: int):
    return {prime: exp * power for prime, exp in base_factors.items()}
