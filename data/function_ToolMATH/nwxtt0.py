def distance_point_to_plane_b(point: tuple[float, float, float], plane_normal: tuple[float, float, float], plane_constant: float) -> float:
    import math
    numerator = abs(sum(p * n for p, n in zip(point, plane_normal)) + plane_constant)
    denominator = math.sqrt(sum(n**2 for n in plane_normal))
    return numerator / denominator
