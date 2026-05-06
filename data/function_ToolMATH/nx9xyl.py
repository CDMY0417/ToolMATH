def prime_factorization_ax(n: int) -> dict:
    factors = {}
    divisor = 2
    while n >= divisor * divisor:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
    if n > 1:
        factors[n] = 1
    return factors
