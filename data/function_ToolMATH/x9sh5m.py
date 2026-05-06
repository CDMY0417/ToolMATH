def am_gm_inequality_lower_bound(products: list[float]) -> float:
    from math import prod
    n = len(products)
    return n * (prod(products) ** (1/n))
