def prime_factorization_cw(number: int):
    from collections import defaultdict
    factors = defaultdict(int)
    factor = 2
    while number > 1:
        while number % factor == 0:
            factors[factor] += 1
            number //= factor
        factor += 1
    return dict(factors)
