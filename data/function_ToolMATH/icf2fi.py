def cancel_common_factors_a(numerator_factors: dict[str, int], denominator_factors: dict[str, int]):
    for factor in numerator_factors:
        if factor in denominator_factors:
            min_power = min(numerator_factors[factor], denominator_factors[factor])
            numerator_factors[factor] -= min_power
            numerator_factors[factor] = max(numerator_factors[factor], 0)
            denominator_factors[factor] -= min_power
            denominator_factors[factor] = max(denominator_factors[factor], 0)
    return numerator_factors, denominator_factors
