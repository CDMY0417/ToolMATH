def closest_point_on_plane(a: float, b: float, c: float, d: float, px: float, py: float, pz: float):
    """Return closest point on plane to P."""
    # plane: a x + b y + c z = d
    # projection: P0 = P - t n, t = (n·P - d)/||n||^2
    denom = a*a + b*b + c*c
    t = (a*px + b*py + c*pz - d) / denom
    return [px - t*a, py - t*b, pz - t*c]
