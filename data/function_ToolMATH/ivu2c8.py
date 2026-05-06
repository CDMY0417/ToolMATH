def cylindrical_to_rectangular(r: float, theta: float, z: float):
    import math
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y, z)
