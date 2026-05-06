import math

def tangent_length_from_origin_to_circle(points):
    """Return tangent length from origin to circle through three points."""
    (x1,y1),(x2,y2),(x3,y3)=points
    # Compute circle center using perpendicular bisectors
    # Solve for center (h,k)
    # Use determinant formula
    def det(a,b,c,d):
        return a*d-b*c
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = (x2*x2 - x1*x1 + y2*y2 - y1*y1)/2.0
    F = (x3*x3 - x1*x1 + y3*y3 - y1*y1)/2.0
    denom = det(A,B,C,D)
    if denom == 0:
        raise ValueError("Points are collinear.")
    h = det(E,B,F,D)/denom
    k = det(A,E,C,F)/denom
    r = math.hypot(x1-h,y1-k)
    d0 = math.hypot(h,k)
    if d0 < r:
        raise ValueError("Origin inside circle.")
    return math.sqrt(d0*d0 - r*r)
