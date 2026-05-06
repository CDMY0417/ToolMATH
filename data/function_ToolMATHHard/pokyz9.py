import math

def shortest_side_length_triangle_from_points(p1, p2, p3):
    # Compute shortest side length of triangle from three points
    def dist(a,b):
        return math.hypot(a[0]-b[0], a[1]-b[1])
    d12 = dist(p1,p2)
    d13 = dist(p1,p3)
    d23 = dist(p2,p3)
    return min(d12, d13, d23)
