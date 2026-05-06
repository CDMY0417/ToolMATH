def compute_outer_diameter(inner_radius: float, widths: list[float]) -> float:
    total_radius = inner_radius + sum(widths)
    return 2 * total_radius
