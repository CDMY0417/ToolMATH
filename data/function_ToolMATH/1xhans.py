def heron_area_squared(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    return s * (s - a) * (s - b) * (s - c)
