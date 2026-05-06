def prime_factorization_bs(n: int):
    factors = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
    return factors
