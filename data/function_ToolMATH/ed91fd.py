def prime_factorization_ab(n: int) -> dict:
    from collections import defaultdict
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return dict(factors)
