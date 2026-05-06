import math

def distance_point_to_line_3d_a(p, p0, d):
    # Distance from point to line in 3D
    vx = p[0]-p0[0]
    vy = p[1]-p0[1]
    vz = p[2]-p0[2]
    cx = vy*d[2] - vz*d[1]
    cy = vz*d[0] - vx*d[2]
    cz = vx*d[1] - vy*d[0]
    num = math.sqrt(cx*cx + cy*cy + cz*cz)
    den = math.sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2])
    if den == 0:
        raise ValueError('direction vector must be nonzero')
    return num / den
