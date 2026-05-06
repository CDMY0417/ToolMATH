def product_of_exponents(factor_dict: dict[int, int]) -> int:
    product = 1
    for base, exponent in factor_dict.items():
        product *= base ** exponent
    return product
