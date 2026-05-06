def triangle_centroid(ax: float, ay: float, bx: float, by: float, cx: float, cy: float):
    """Return centroid (x,y)."""
    return [(ax + bx + cx) / 3.0, (ay + by + cy) / 3.0]
