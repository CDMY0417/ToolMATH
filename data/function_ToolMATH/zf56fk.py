def lattice_points_on_circle(radius_squared: int):
    points = []
    for x in range(-int(radius_squared**0.5), int(radius_squared**0.5) + 1):
        y_squared = radius_squared - x**2
        if y_squared >= 0:
            y = int(y_squared**0.5)
            if y**2 == y_squared:
                points.append((x, y))
                if y != 0:
                    points.append((x, -y))
    return points
