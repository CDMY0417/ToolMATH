def vertex_from_parabola_y2_linear(D: float, E: float, F: float):
    """Return vertex (x_v, y_v) for y^2 + D*y + E*x + F = 0."""
    yv = -D / 2.0
    # substitute yv to solve for x
    x_v = -(yv*yv + D*yv + F) / E
    return [x_v, yv]
