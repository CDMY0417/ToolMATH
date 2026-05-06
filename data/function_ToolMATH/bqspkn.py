def sin_arcsin_sum(x: float, y: float) -> float:
    cos_x = (1 - x ** 2) ** 0.5
    cos_y = (1 - y ** 2) ** 0.5
    return x * cos_y + cos_x * y
