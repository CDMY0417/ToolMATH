def prime_factorization_ca(n: int):
    factors = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    return factors
