def prime_factors_ad(n: int):
    factors = {}
    d = 2
    while n >= 2:
        if n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        else:
            d += 1
    return factors
