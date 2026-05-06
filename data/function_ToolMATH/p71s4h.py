def compare_pipe_volumes(large_diameter: float, small_diameter: float) -> int:
    large_radius = large_diameter / 2
    small_radius = small_diameter / 2
    return int((large_radius ** 2) / (small_radius ** 2))
