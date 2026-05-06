def is_right_triangle_i(a: float, b: float, c: float) -> bool:
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9
