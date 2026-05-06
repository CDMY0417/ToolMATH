def apply_am_gm_inequality_for_three_terms(x: float, y: float, z: float):
    geo_mean = (x * y * z) ** (1/3)
    inequality_expression = x + y + z >= 3 * geo_mean
    return geo_mean, inequality_expression
