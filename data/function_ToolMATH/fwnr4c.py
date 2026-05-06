def factorial_prime_factorization(n: int):
    from collections import defaultdict
    def prime_factors(x):
        factors = defaultdict(int)
        d = 2
        while x >= d * d:
            while x % d == 0:
                factors[d] += 1
                x //= d
            d += 1
        if x > 1:
            factors[x] += 1
        return factors
    total_factors = defaultdict(int)
    for i in range(2, n + 1):
        factors = prime_factors(i)
        for p, exp in factors.items():
            total_factors[p] += exp
    return dict(total_factors)
