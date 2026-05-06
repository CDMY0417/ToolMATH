def number_of_factors(exponents: list[int]) -> int:
    result = 1
    for exponent in exponents:
        result *= (exponent + 1)
    return result
