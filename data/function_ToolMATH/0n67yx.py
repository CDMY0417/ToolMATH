def triangle_area_from_sides(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
