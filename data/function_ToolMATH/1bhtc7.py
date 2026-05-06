def greatest_common_factor(pf1: dict, pf2: dict) -> int:
    gcf = 1
    common_primes = set(pf1.keys()).intersection(set(pf2.keys()))
    for prime in common_primes:
        gcf *= prime ** min(pf1[prime], pf2[prime])
    return gcf
