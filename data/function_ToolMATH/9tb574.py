def lcm_from_prime_factors(factors1: dict[int, int], factors2: dict[int, int]) -> int:
    from collections import defaultdict
    lcm_factors = defaultdict(int)
    all_primes = set(factors1.keys()).union(set(factors2.keys()))
    for prime in all_primes:
        lcm_factors[prime] = max(factors1.get(prime, 0), factors2.get(prime, 0))
    lcm = 1
    for prime, exp in lcm_factors.items():
        lcm *= prime ** exp
    return lcm
