def frustum_volume_from_ratios(original_volume: float, removed_ratio: float):
    remaining_ratio = 1 - removed_ratio
    return original_volume * remaining_ratio
