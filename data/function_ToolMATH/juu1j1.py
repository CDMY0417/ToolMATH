def dot_product_u(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))
