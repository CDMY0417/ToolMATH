def divide_prime_factors(factors_a: dict[int, int], factors_b: dict[int, int]) -> dict[int, int]:
    from collections import defaultdict
    result = defaultdict(int, factors_a)
    for prime, count in factors_b.items():
        result[prime] -= count
        if result[prime] <= 0:
            result.pop(prime)
    return dict(result)
