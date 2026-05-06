def polar_to_rectangular_b(r: float, theta: float):
    import math
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
