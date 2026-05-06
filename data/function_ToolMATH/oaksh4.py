def ellipse_focus(a_squared: float, b_squared: float) -> float:
    import math
    c = math.sqrt(abs(a_squared - b_squared))
    return c
