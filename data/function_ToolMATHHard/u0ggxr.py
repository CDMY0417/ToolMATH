def closest_point_on_line_3d(p0, d, q):
    # Closest point on line p0 + t d to point q
    denom = d[0]*d[0] + d[1]*d[1] + d[2]*d[2]
    if denom == 0:
        raise ValueError('direction vector must be nonzero')
    t = ((q[0]-p0[0])*d[0] + (q[1]-p0[1])*d[1] + (q[2]-p0[2])*d[2]) / denom
    return [p0[0] + t*d[0], p0[1] + t*d[1], p0[2] + t*d[2]]
