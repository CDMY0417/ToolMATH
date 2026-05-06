def distance_point_to_plane(point: tuple[float, float, float], plane_coefficients: tuple[float, float, float, float]) -> float:
    A, B, C, D = plane_coefficients
    x0, y0, z0 = point
    numerator = abs(A * x0 + B * y0 + C * z0 + D)
    denominator = (A**2 + B**2 + C**2) ** 0.5
    return numerator / denominator
