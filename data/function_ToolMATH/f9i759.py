def cube_sum_with_mixed_product_terms(x_plus_y: int, xy: int) -> int:
    mixed_product_terms = 3 * (xy) * (x_plus_y)
    cube_sum = (x_plus_y) ** 3 - mixed_product_terms
    return cube_sum
