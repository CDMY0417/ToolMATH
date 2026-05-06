def direction_parameter_a_from_two_points(p1, p2):
    # Given two points, return a so direction is (a, -1)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dy == 0:
        raise ValueError('direction has dy=0, cannot scale to -1')
    return dx / (-dy)
