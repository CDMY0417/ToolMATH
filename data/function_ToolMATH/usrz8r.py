def least_common_multiple_ab(a_factors: dict[int, int], b_factors: dict[int, int]) -> int:
    lcm = 1
    all_primes = set(a_factors.keys()).union(set(b_factors.keys()))
    for prime in all_primes:
        lcm *= prime ** max(a_factors.get(prime, 0), b_factors.get(prime, 0))
    return lcm
