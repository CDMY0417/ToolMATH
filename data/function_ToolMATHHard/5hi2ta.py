import math

def area_of_planar_quadrilateral(points):
    'Compute area of a planar quadrilateral given 4 ordered points in 3D.'
    if len(points) != 4:
        raise ValueError('points must have length 4')
    def cross(u, v):
        return [
            u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0],
        ]
    def norm(u):
        return math.sqrt(sum(ui*ui for ui in u))
    p0 = points[0]
    def sub(p, q):
        return [p[i]-q[i] for i in range(3)]
    v1 = sub(points[1], p0)
    v2 = sub(points[2], p0)
    v3 = sub(points[3], p0)
    area1 = 0.5 * norm(cross(v1, v2))
    area2 = 0.5 * norm(cross(v2, v3))
    return area1 + area2
