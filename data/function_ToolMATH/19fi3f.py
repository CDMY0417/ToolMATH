def lcm_from_factors(factors_a: dict[int, int], factors_b: dict[int, int]) -> int:
    lcm_factors = {}
    for prime in set(factors_a) | set(factors_b):
        lcm_factors[prime] = max(factors_a.get(prime, 0), factors_b.get(prime, 0))
    lcm = 1
    for prime, power in lcm_factors.items():
        lcm *= prime ** power
    return lcm
