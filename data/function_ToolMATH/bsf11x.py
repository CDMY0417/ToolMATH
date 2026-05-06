def solve_right_triangle_a(hypotenuse: float, known_side: float) -> float:
    import math
    unknown_side = math.sqrt(hypotenuse**2 - known_side**2)
    return unknown_side
