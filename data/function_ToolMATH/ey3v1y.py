def centroid_of_triangle_a(A: tuple, B: tuple, C: tuple) -> tuple:
    return tuple((a + b + c) / 3 for a, b, c in zip(A, B, C))
