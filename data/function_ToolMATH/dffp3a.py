def multiply_factors(coef1: float, power1: int, coef2: float, power2: int) -> float:
    product_coef = coef1 * coef2
    product_power = power1 + power2
    return product_coef * (10 ** product_power)
