def convert_to_polar(x: float, y: float) -> tuple:
    import math
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return (r, theta)
