def prime_factorization_q(n: int) -> dict:
    factors = {}
    divisor = 2
    while n >= 2:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors[divisor] = count
        divisor += 1
    return factors
