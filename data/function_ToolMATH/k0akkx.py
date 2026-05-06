def prime_factorization_am(n: int) -> dict:
    from collections import defaultdict
    factors = defaultdict(int)
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 1:
        factors[n] += 1
    return dict(factors)
