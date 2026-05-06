def evaluate_polynomial_product(x: int, roots: list[int]) -> int:
    result = 1
    for root in roots:
        result *= (x - root)
    return result
