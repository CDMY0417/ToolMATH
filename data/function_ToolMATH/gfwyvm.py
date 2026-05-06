def distance_point_to_plane_a(x: float, y: float, z: float, a: float, b: float, c: float, d: float) -> float:
    numerator = abs(a * x + b * y + c * z + d)
    denominator = (a**2 + b**2 + c**2)**0.5
    return numerator / denominator
