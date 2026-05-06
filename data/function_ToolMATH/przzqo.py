def sum_to_product_formula_sin(x: float, z: float) -> float:
    from math import sin, cos, radians
    return 2 * sin(radians((x - z) / 2)) * cos(radians((x + z) / 2))
