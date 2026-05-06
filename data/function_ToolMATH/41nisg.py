def compute_point_on_parametric_circle(t: float) -> tuple:
    x = (1 - t**2) / (1 + t**2)
    y = (2 * t) / (1 + t**2)
    return (x, y)
