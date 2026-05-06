def is_isosceles_right_triangle(a: float, b: float, c: float) -> bool:
    sides = sorted([a, b, c])
    return sides[0] == sides[1] and abs(sides[2] - sides[0] * (2 ** 0.5)) < 1e-6
