def find_vertical_asymptotes(numerator_factors: dict, denominator_factors: dict) -> int:
    vertical_asymptotes = 0
    for factor in denominator_factors:
        if factor not in numerator_factors or denominator_factors[factor] > numerator_factors.get(factor, 0):
            vertical_asymptotes += 1
    return vertical_asymptotes
