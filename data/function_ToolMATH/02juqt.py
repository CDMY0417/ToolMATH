def prime_factorize_b(n: int):
    factorization = []
    d = 2
    while n >= 2:
        exponent = 0
        while (n % d) == 0:
            n //= d
            exponent += 1
        if exponent > 0:
            factorization.append((d, exponent))
        d += 1
    return factorization
