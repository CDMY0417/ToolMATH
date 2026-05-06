def centroid_of_triangle(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> tuple[float, float]:
    return tuple((a[i] + b[i] + c[i]) / 3 for i in range(len(a)))
