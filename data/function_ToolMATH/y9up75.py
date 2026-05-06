def sum_to_product_cos_a(angle1: float, angle2: float) -> float:
    import math
    return 2 * math.cos(math.radians((angle1 + angle2) / 2)) * math.cos(math.radians((angle2 - angle1) / 2))
