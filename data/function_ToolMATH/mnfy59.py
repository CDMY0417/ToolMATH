def scale_base_and_area(base1: int, ratio_a: int, ratio_b: int) -> tuple:
    base2 = base1 * ratio_b // ratio_a
    scale_factor = ratio_b / ratio_a
    return base2, scale_factor
