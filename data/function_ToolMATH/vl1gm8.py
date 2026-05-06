def sum_to_product_formula_a(angle_a: float, angle_b: float):
    from math import sin, radians
    return -2 * sin(radians((angle_a + angle_b) / 2)) * sin(radians((angle_a - angle_b) / 2))
