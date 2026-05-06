def additional_factors_for_square(factor_exponents: dict) -> list:
    return [factor for factor, exp in factor_exponents.items() if exp % 2 != 0]
