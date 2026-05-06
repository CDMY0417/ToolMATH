def determinant_3x3_a(a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, i: float) -> float:
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
