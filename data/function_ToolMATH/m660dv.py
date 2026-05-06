def greatest_common_factor_from_factors(common_factors: dict[int, int]) -> int:
    gcf = 1
    for prime, power in common_factors.items():
        gcf *= prime ** power
    return gcf
