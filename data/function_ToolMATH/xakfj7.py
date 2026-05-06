def factor_int(n: int):
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors
