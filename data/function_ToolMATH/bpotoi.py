def prime_factorization_w(n: int):
    factors = {}
    divisor = 2
    while n >= 2:
        if n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        else:
            divisor += 1
    return factors
