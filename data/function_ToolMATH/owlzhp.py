def prime_factors_au(n: int) -> set:
    i = 2
    factors = set()
    while i * i <= n:
        while (n % i) == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors
