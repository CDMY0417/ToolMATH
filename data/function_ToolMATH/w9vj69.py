def evaluate_polynomial_at_value_a(roots: list[float], constant: float, x: float) -> float:
    product = constant
    for root in roots:
        product *= (x - root)
    return product
