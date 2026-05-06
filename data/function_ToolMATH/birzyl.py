def expand_binomial_product_b(a: int, b: int, c: int, d: int) -> tuple:
    return (a * c, a * d + b * c, b * d)
