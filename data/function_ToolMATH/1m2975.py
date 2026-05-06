def sum_to_product_formula_c(angle_a: float, angle_b: float):
    import math
    return 2 * math.sin(math.radians((angle_a + angle_b) / 2)) * math.cos(math.radians((angle_a - angle_b) / 2))
