def sphere_radius_from_surface_area_a(surface_area: float) -> float:
    radius_squared = surface_area / (4 * 3.141592653589793)
    radius = radius_squared ** 0.5
    return radius
