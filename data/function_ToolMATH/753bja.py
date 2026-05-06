def x_intersection_points(x_min: float, x_max: float) -> int:
    from math import pi
    count = 0
    n = 0
    while True:
        x = (4 * n + 1) * pi / 4
        if x_min <= x <= x_max:
            count += 1
        elif x > x_max:
            break
        n += 1
    return count
