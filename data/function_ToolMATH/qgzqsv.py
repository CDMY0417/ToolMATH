def prime_factorization_bf(n: int):
    factors = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor not in factors:
                factors[divisor] = 0
            factors[divisor] += 1
            n //= divisor
        divisor += 1
    return factors
