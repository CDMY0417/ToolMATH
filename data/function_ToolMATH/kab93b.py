def factorial_prime_factors(n: int):
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
    result = defaultdict(int)
    for i in range(2, n + 1):
        for prime, count in prime_factors(i).items():
            result[prime] += count
    return dict(result)
