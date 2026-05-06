def lcm_from_factors_a(factors1: dict[int, int], factors2: dict[int, int]) -> int:
    lcm_factors = {}
    for p in set(factors1).union(factors2):
        lcm_factors[p] = max(factors1.get(p, 0), factors2.get(p, 0))
    lcm = 1
    for p, power in lcm_factors.items():
        lcm *= p ** power
    return lcm
