def prime_factorization_bj(n: int) -> dict:
    from collections import defaultdict
    i = 2
    factors = defaultdict(int)
    while i * i <= n:
        while (n % i) == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return dict(factors)
