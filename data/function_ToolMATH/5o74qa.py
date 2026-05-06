def prime_factorization_cl(n: int) -> dict:
    factors = {}
    d = 2
    while n >= 2:
        while (n % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1
    return factors
