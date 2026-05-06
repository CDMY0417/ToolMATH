def convert_polar_to_rectangular(r: float, theta: float):
    import math
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
