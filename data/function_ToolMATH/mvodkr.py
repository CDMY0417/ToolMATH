def cone_surface_area(radius: float, slant_height: float) -> float:
    base_area = 3.14159 * radius**2
    lateral_area = 3.14159 * radius * slant_height
    return base_area + lateral_area
