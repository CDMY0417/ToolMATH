def factorial_prime_factors_a(n: int):
    from collections import defaultdict
    factors = defaultdict(int)
    for i in range(2, n + 1):
        num = i
        factor = 2
        while num > 1:
            while num % factor == 0:
                factors[factor] += 1
                num //= factor
            factor += 1
    return dict(factors)
