def cube_volume_difference_by_scale_factor(volume: int, scale_factor: int) -> int:
    scaled_volume = scale_factor ** 3 * volume
    return scaled_volume - volume
