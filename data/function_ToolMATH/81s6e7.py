def combine_fraction_numerators_and_denominators(numerator_factors: dict[int, int], denominator_factors: dict[int, int]) -> dict[int, int]:
    combined_factors = numerator_factors.copy()
    for factor, exponent in denominator_factors.items():
        combined_factors[factor] = combined_factors.get(factor, 0) - exponent
        if combined_factors[factor] == 0:
            del combined_factors[factor]
    return combined_factors
