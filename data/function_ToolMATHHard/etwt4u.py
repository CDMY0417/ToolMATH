def centroid_of_points(points):
    """Return average of points."""
    if not points:
        raise ValueError("Points list is empty.")
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    n = len(points)
    return [sx / n, sy / n]
