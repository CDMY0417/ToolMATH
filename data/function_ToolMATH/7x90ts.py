def polynomial_roots_product(roots: list[float]) -> float:
    product = 1
    for root in roots:
        product *= root
    return product
