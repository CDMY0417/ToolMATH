def triangle_area_by_angles(side: float, angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    return (side ** 2 * math.sin(angle_radians)) / 2
