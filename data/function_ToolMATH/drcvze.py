def prime_factorization_z(n: int):
    i = 2
    factors = []
    while i * i <= n:
        count = 0
        while (n % i) == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors
