def cross_product_c(v1: list[float], v2: list[float]) -> list[float]:
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return [y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2]
