def convert_units_c(amount: float, conversion_factors: list[float]):
    result = amount
    for factor in conversion_factors:
        result *= factor
    return result
