def common_prime_factors(pf1: dict[int, int], pf2: dict[int, int]) -> dict[int, int]:
    return {p: min(pf1[p], pf2[p]) for p in pf1 if p in pf2}
