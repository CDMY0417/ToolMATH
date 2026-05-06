def area_of_triangle_b(v1: tuple[float, float, float], v2: tuple[float, float, float], v3: tuple[float, float, float]) -> float:
    import math
    # Use the cross product of vectors to determine area
    ax, ay, az = v1
    bx, by, bz = v2
    cx, cy, cz = v3
    # Vectors AB and AC
    abx, aby, abz = bx - ax, by - ay, bz - az
    acx, acy, acz = cx - ax, cy - ay, cz - az
    # Cross product AB x AC
    cross_x = aby * acz - abz * acy
    cross_y = abz * acx - abx * acz
    cross_z = abx * acy - aby * acx
    # Magnitude of cross product is 2 times the area of the triangle
    cross_mag = math.sqrt(cross_x ** 2 + cross_y ** 2 + cross_z ** 2)
    return 0.5 * cross_mag
