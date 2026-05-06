def dot_product_m(v: list[float], w: list[float]) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
