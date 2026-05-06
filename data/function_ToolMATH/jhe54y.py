def factorization(n: int):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
