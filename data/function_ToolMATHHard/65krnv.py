def intersection_point_param_lines_2d(p1, d1, p2, d2):
    'Find intersection point of two 2D parametric lines.'
    a11, a12 = d1[0], -d2[0]
    a21, a22 = d1[1], -d2[1]
    b1 = p2[0] - p1[0]
    b2 = p2[1] - p1[1]
    det = a11*a22 - a12*a21
    if det == 0:
        raise ValueError('Lines are parallel or coincident')
    t = (b1*a22 - b2*a12) / det
    return [p1[0] + t*d1[0], p1[1] + t*d1[1]]
