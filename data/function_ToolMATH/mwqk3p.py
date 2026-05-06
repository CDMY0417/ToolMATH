def cross_product_f(v: list[float], w: list[float]) -> list[float]:
    return [v[1] * w[2] - v[2] * w[1], v[2] * w[0] - v[0] * w[2], v[0] * w[1] - v[1] * w[0]]
