import math

def right_triangle_tangent_circle_cp(AB: float, BC: float):
    """Return CP length for circle centered on AB tangent to BC and AC."""
    if AB <= 0 or BC <= 0:
        raise ValueError("AB and BC must be positive.")
    # Coordinates: B(0,0), A(AB,0), C(0,BC)
    # Line AC: BC*x + AB*y - AB*BC = 0
    # Center O=(t,0), tangent to BC => radius=t
    hyp = math.hypot(AB, BC)
    t = AB * BC / (BC + hyp)
    # Projection of O onto line AC
    # Line in form ax+by+c=0 with a=BC, b=AB, c=-AB*BC
    a = BC
    b = AB
    c = -AB * BC
    x0, y0 = t, 0.0
    denom = a*a + b*b
    x = x0 - a*(a*x0 + b*y0 + c)/denom
    y = y0 - b*(a*x0 + b*y0 + c)/denom
    # Distance from C to P
    return math.hypot(x - 0.0, y - BC)
