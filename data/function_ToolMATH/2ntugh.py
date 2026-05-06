def unwrapped_cone_coordinates(distance: float, angle: float):
    import math
    x = distance * math.cos(angle)
    y = distance * math.sin(angle)
    return (x, y)
