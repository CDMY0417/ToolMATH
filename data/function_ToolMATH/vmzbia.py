def sum_to_product_cos(angle1: float, angle2: float):
    from math import cos, radians
    return 2 * cos(radians((angle1 + angle2) / 2)) * cos(radians((angle1 - angle2) / 2))
