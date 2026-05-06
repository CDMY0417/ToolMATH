def prime_factor_exponents(n: int):
    exponents = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            if d in exponents:
                exponents[d] += 1
            else:
                exponents[d] = 1
            n //= d
        d += 1
    if n > 1:
        exponents[n] = 1
    return exponents
