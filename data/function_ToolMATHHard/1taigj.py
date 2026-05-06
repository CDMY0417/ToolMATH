import math

def distance_between_points_3d(p, q):
    # Compute distance between two 3D points
    dx = p[0]-q[0]
    dy = p[1]-q[1]
    dz = p[2]-q[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)
