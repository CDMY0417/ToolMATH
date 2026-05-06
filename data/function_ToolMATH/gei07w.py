def prime_factorization_da(n: int) -> dict:
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors[n] = 1
            break
    return factors
