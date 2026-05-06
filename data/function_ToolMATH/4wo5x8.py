def ring_area(outer_radius: float, inner_radius: float) -> float:
    import math
    return math.pi * (outer_radius**2 - inner_radius**2)
