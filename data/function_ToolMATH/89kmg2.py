def rotate_point(degrees: float) -> tuple:
    import math
    radians = math.radians(degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
