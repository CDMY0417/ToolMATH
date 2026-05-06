def shaded_region_area(grid_area: float, triangle_base: float, triangle_height: float) -> float:
    triangle_area = 0.5 * triangle_base * triangle_height
    return grid_area - triangle_area
