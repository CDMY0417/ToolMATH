def lattice_points_on_circle_a(radius: float):
    points = []
    for x in range(-int(radius), int(radius) + 1):
        y_square = radius**2 - x**2
        if y_square >= 0:
            y = int(y_square ** 0.5)
            if y_square == y ** 2:  # Check if y is an integer
                points.extend([(x, y), (x, -y), (-x, y), (-x, -y)])
    return list(set(points))
