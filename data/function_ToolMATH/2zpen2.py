def points_within_circle(max_radius_squared: float):
    points = []
    max_radius = int(max_radius_squared**0.5)
    for x in range(-max_radius, max_radius + 1):
        for y in range(-max_radius, max_radius + 1):
            if x**2 + y**2 <= max_radius_squared:
                points.append((x, y))
    return points
