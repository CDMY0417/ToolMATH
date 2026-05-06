def total_surface_area_after_removal(initial_surface_area: int, cubes_removed: int, surface_area_per_cube: int):
    return initial_surface_area - cubes_removed * surface_area_per_cube
