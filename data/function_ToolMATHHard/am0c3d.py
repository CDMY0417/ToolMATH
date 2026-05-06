from fractions import Fraction

def barycentric_coords_intersection_from_side_ratios(ae: int, ec: int, af: int, fb: int):
    # Return (x,y,z) so P = xA + yB + zC for intersection of BE and CF
    # Use A=(1,0,0), B=(0,1,0), C=(0,0,1)
    A = (Fraction(1), Fraction(0), Fraction(0))
    B = (Fraction(0), Fraction(1), Fraction(0))
    C = (Fraction(0), Fraction(0), Fraction(1))
    t = Fraction(ae, ae+ec)
    E = (A[0]*(1-t) + C[0]*t, A[1]*(1-t) + C[1]*t, A[2]*(1-t) + C[2]*t)
    u = Fraction(af, af+fb)
    F = (A[0]*(1-u) + B[0]*u, A[1]*(1-u) + B[1]*u, A[2]*(1-u) + B[2]*u)
    ex, ey, ez = E
    fx, fy, fz = F
    # Solve B + s(E-B) = C + r(F-C)
    # x: s*ex = r*fx
    # y: 1 + s*(ey-1) = r*fy
    if fx == 0:
        raise ValueError('Degenerate configuration')
    denom = (ey-1) - (ex*fy/fx)
    s = Fraction(-1, 1) / denom
    # compute P
    Px = B[0] + s*(E[0]-B[0])
    Py = B[1] + s*(E[1]-B[1])
    Pz = B[2] + s*(E[2]-B[2])
    return [float(Px), float(Py), float(Pz)]
