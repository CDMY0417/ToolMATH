def line_coefficients_from_point_direction(x0: float, y0: float, vx: float, vy: float):
    """Return [A,B,C] for line through (x0,y0) in direction (vx,vy)."""
    # Normal vector is (vy, -vx)
    A = vy
    B = -vx
    C = -(A*x0 + B*y0)
    return [A, B, C]
