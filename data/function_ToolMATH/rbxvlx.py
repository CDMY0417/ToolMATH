def scale_ingredients(ratios: tuple, scale_factor: int):
    return tuple(part * scale_factor for part in ratios)
