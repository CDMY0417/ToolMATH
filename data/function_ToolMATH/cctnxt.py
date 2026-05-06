def compute_ratio_a(x: int, y: int, z: int) -> float:
    numerator = x * y + y * z + z * x
    denominator = x ** 2 + y ** 2 + z ** 2
    return numerator / denominator
