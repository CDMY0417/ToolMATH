def plane_through_two_points_perp_to_plane(p1, p2, plane_normal):
    # Plane through p1,p2 and perpendicular to plane_normal
    v = [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    n1 = plane_normal
    A = v[1]*n1[2] - v[2]*n1[1]
    B = v[2]*n1[0] - v[0]*n1[2]
    C = v[0]*n1[1] - v[1]*n1[0]
    D = -(A*p1[0] + B*p1[1] + C*p1[2])
    # normalize to integers and A>0
    vals = [A,B,C,D]
    vals = [int(round(x)) for x in vals]
    A,B,C,D = vals
    def igcd(a,b):
        a=abs(a); b=abs(b)
        while b:
            a,b = b, a%b
        return a
    g = 0
    for val in [A,B,C,D]:
        g = igcd(g, val)
    if g and g != 1:
        A//=g; B//=g; C//=g; D//=g
    if A < 0:
        A,B,C,D = -A,-B,-C,-D
    return [A,B,C,D]
