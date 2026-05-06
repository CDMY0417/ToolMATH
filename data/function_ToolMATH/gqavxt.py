def simplify_fraction_bj(num_factors: list[int], denom_factors: list[int]) -> float:
    from math import prod
    num_product = prod(num_factors)
    denom_product = prod(denom_factors)
    return num_product / denom_product
