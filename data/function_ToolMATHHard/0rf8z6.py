def plane_equation_from_parametric(p0, d1, d2):
    # Plane through p0 with direction vectors d1, d2
    # normal = d1 x d2
    A = d1[1]*d2[2] - d1[2]*d2[1]
    B = d1[2]*d2[0] - d1[0]*d2[2]
    C = d1[0]*d2[1] - d1[1]*d2[0]
    D = -(A*p0[0] + B*p0[1] + C*p0[2])
    # normalize to gcd and A>0
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
