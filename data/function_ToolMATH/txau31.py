def scale_ratio_b(ratio_base: int, ratio_height: int, desired_base: int) -> float:
    factor = desired_base / ratio_base
    return ratio_height * factor
