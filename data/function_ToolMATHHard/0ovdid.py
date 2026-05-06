def reflect_point_across_plane(point, plane):
    a,b,c,d = plane
    x,y,z = point
    denom = a*a + b*b + c*c
    t = (a*x + b*y + c*z - d) / denom
    px = x - a*t
    py = y - b*t
    pz = z - c*t
    return [2*px - x, 2*py - y, 2*pz - z]
