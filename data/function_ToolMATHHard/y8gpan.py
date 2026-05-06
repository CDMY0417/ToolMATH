def polygon_area(points):
    """Return polygon area by shoelace formula."""
    if len(points) < 3:
        return 0.0
    s = 0.0
    for (x1,y1),(x2,y2) in zip(points, points[1:]+points[:1]):
        s += x1*y2 - x2*y1
    return abs(s) / 2.0
