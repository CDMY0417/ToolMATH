def side_ratios_30_60_90_triangle_a(shorter_side: float):
    longer_side = shorter_side * (3 ** 0.5)
    hypotenuse = 2 * shorter_side
    return longer_side, hypotenuse
