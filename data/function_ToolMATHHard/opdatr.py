def equidistant_point_xz_plane(p1, p2, p3):
    """Return [x,0,z] equidistant from three points."""
    x,z=0.0,0.0
    (x1,y1,z1)=p1; (x2,y2,z2)=p2; (x3,y3,z3)=p3
    # Solve equations: (x-x1)^2+(0-y1)^2+(z-z1)^2 = (x-x2)^2+y2^2+(z-z2)^2
    # Linear in x,z
    A1=2*(x2-x1)
    B1=2*(z2-z1)
    C1=x2*x2+z2*z2+y2*y2 - (x1*x1+z1*z1+y1*y1)
    A2=2*(x3-x1)
    B2=2*(z3-z1)
    C2=x3*x3+z3*z3+y3*y3 - (x1*x1+z1*z1+y1*y1)
    det=A1*B2-A2*B1
    if det==0:
        raise ValueError("No unique solution.")
    x=(C1*B2-C2*B1)/det
    z=(A1*C2-A2*C1)/det
    return [x,0.0,z]
