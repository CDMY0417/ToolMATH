def factorial_ratio_simplify(numerator_factors: list[int], denominator_factors: list[int]) -> int:
    num_product = 1
    denom_product = 1
    for factor in numerator_factors:
        num_product *= factor
    for factor in denominator_factors:
        denom_product *= factor
    return num_product // denom_product
