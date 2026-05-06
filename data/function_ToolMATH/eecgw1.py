def sum_to_product_sin_b(angle1: float, angle2: float) -> float:
    import math
    return 2 * math.sin(math.radians((angle2 - angle1) / 2)) * math.cos(math.radians((angle1 + angle2) / 2))
