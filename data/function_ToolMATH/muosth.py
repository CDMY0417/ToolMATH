def decompose_to_prime_factors(n: int) -> dict:
    factors = {}
    divisor = 2
    while n >= 2:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
    return factors
