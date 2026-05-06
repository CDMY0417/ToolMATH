def prime_factors_a(n: int) -> list:
    i = 2
    factors = set()
    while n % i == 0:
        factors.add(i)
        n //= i
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
    if n > 2:
        factors.add(n)
    return list(factors)
