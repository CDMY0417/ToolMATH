def sum_to_product_formula_b(a: float, b: float) -> float:
    from math import sin, cos, radians
    sum_term = 2 * sin(radians((a + b) / 2)) * cos(radians((a - b) / 2))
    return sum_term
