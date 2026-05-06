def plane_through_line_and_point(P1, P2, point):
    # Plane is combination: a*P1 + b*P2 = 0. Solve for a,b so point satisfies.
    a1,b1,c1,d1 = P1
    a2,b2,c2,d2 = P2
    x,y,z = point
    # a*(a1x+b1y+c1z+d1) + b*(a2x+b2y+c2z+d2)=0
    s1 = a1*x + b1*y + c1*z + d1
    s2 = a2*x + b2*y + c2*z + d2
    # take a = s2, b = -s1
    A = s2*a1 - s1*a2
    B = s2*b1 - s1*b2
    C = s2*c1 - s1*c2
    D = s2*d1 - s1*d2
    # normalize sign A>0 if possible
    if A < 0:
        A,B,C,D = -A,-B,-C,-D
    return [A,B,C,D]
