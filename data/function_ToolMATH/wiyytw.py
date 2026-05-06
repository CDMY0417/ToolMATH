def number_of_divisors(exponents: list[int]) -> int:
    product = 1
    for exp in exponents:
        product *= (exp + 1)
    return product
