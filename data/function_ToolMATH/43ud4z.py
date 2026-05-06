def dot_product_bb(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))
